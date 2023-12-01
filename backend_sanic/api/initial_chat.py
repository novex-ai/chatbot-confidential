from sanic import Blueprint, Request
from sanic.log import logger
from sanic_ext import openapi
from sqlalchemy import select, func

from backend_sanic.chat_util import pipe_generated_response
from backend_sanic.models import FileUpload


bp = Blueprint("initial_chat")


@bp.route("/initial_chat", methods={"POST"})
@openapi.definition(
    response=openapi.response(
        200, {"text/plain": str}, "Returns chunked chat completion text"
    ),
)
async def initial_chat(request: Request):
    """Generate initial chat-like text"""
    num_file_uploads = await _get_num_file_uploads(request.ctx.session)
    sanic_response = await request.respond(content_type="text/plain")
    if num_file_uploads > 0:
        prompt_msg = f"""
        Please say: {num_file_uploads} documents have been processed, and that we are ready to answer questions.
        """
        complete_text = await pipe_generated_response(prompt_msg, sanic_response)
    else:
        prompt_msg = """
        You are a helpful knowledge chatbot.
        Please introduce yourself and ask the user to click on the Data tab and upload documents.
        """
        complete_text = await pipe_generated_response(prompt_msg, sanic_response)
    logger.info(f"handled {prompt_msg=} with {complete_text=}")


async def _get_num_file_uploads(session):
    async with session.begin():
        result = await session.execute(select(func.count()).select_from(FileUpload))
        num_file_uploads = result.scalar_one()
    return num_file_uploads
