from dataclasses import dataclass
import json

from sanic import Blueprint, Request
from sanic.response import text as text_response
from sanic.log import logger
from sanic_ext import openapi, validate
from sqlalchemy import select

from backend_sanic.api_generate import generate_text
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
    chat_embedding = string_to_embeddings(chat_msg)
    logger.info(f"{chat_msg=} {chat_embedding=}")
    session = request.ctx.session
    async with session.begin():
        distance_col = EmbeddedChunk.vector.l2_distance(chat_embedding).label(
            "distance"
        )
        result = await session.scalars(
            select(
                EmbeddedChunk,
                distance_col,
            )
            .filter(distance_col < 1.0)
            .order_by(distance_col.asc())
            .limit(4)
        )
        rows = result.all()
        logger.info(f"{rows=}")
    if len(rows) > 0:
        close_texts = [chunk.chunk_text for (chunk, _) in rows]
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
    complete_text = ""
    async with generate_text(prompt_msg, stream=True) as response:
        if response.status != 200:
            response_json = await response.json()
            logger.error(f"error from {response.url=} {response_json=}")
            response.raise_for_status()
        async for data in response.content.iter_any():
            data_str = data.decode("utf-8")
            data_obj = json.loads(data_str)
            response_text = data_obj["response"]
            complete_text += response_text
            await sanic_response.send(response_text)
    await sanic_response.eof()
    logger.info(f"handled {prompt_msg=} with {complete_text=}")
