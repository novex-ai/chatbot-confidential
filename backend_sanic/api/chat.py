from dataclasses import dataclass

from sanic import Blueprint, Request
from sanic.response import text as text_response
from sanic.log import logger
from sanic_ext import openapi, validate
from sqlalchemy import select

from backend_sanic.api_generate import generate_text
from backend_sanic.chat_util import pipe_generated_response
from backend_sanic.embeddings import string_to_embeddings
from backend_sanic.models import EmbeddedChunk


@dataclass
class ChatRequest:
    msg: str


bp = Blueprint("chat")


@bp.route("/chat", methods={"POST"})
@openapi.definition(
    body={"application/json": ChatRequest},
    response=openapi.response(
        200, {"text/plain": str}, "Returns chunked chat completion text"
    ),
)
@validate(json=ChatRequest)
async def chat(request: Request, body: ChatRequest):
    """Generate text from a prompt msg"""
    logger.info(f"handling {body=}")
    chat_msg = body.msg
    if not chat_msg:
        logger.error(f"{chat_msg=} not provided in {body=} {request.body=}")
        return text_response("error: msg not provided", status=400)
    close_chunks = await _select_close_chunks(request.ctx.session, chat_msg)
    if chat_msg.endswith("?"):
        hyde_response_text = await _generate_hyde_response_text(chat_msg)
        close_chunks += await _select_close_chunks(
            request.ctx.session, hyde_response_text
        )
    if len(close_chunks) > 0:
        close_texts = [chunk.chunk_text for chunk in close_chunks]
        context = "\n###\n".join(close_texts)
        prompt_msg = f"""Use the following pieces of context to answer the
question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {chat_msg}
"""
    elif chat_msg.endswith("?"):
        prompt_msg = f"""
Answer the following question.  If you don't know the answer, just say that you don't know, don't try to make up an answer.
Question: {chat_msg}"""
    else:
        prompt_msg = chat_msg
    sanic_response = await request.respond(content_type="text/plain")
    complete_text = await pipe_generated_response(prompt_msg, sanic_response)
    logger.info(f"handled {prompt_msg=} with {complete_text=}")


async def _generate_hyde_response_text(chat_msg: str):
    """
    Generate a response to a question using HyDE
    https://arxiv.org/pdf/2212.10496.pdf
    """
    hyde_prompt_msg = f"write a paragraph that answers the question: {chat_msg}"
    async with generate_text(hyde_prompt_msg, stream=False) as response:
        if response.status != 200:
            response_json = await response.json()
            logger.error(f"error from {response.url=} {response_json=}")
            response.raise_for_status()
        data = await response.json()
        hyde_response_text = data["response"]
    return hyde_response_text


async def _select_close_chunks(
    session, search_str: str, max_distance: float = 0.1, limit: int = 4
):
    search_embedding = string_to_embeddings(search_str)
    async with session.begin():
        distance_col = EmbeddedChunk.vector.cosine_distance(search_embedding).label(
            "distance"
        )
        result = await session.execute(
            select(
                EmbeddedChunk,
                distance_col,
            )
            .filter(distance_col < max_distance)
            .order_by(distance_col.asc())
            .limit(limit)
        )
        embedded_chunk_rows = result.all()
    logger.info(f"selecting close chunks {search_str=} {embedded_chunk_rows=}")
    close_chunks = [chunk for (chunk, _) in embedded_chunk_rows]
    return close_chunks
