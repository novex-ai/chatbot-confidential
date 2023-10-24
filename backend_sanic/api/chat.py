from dataclasses import dataclass
import json
import os

import aiohttp
from sanic import Blueprint, Request
from sanic.response import text as text_response
from sanic.log import logger
from sanic_ext import openapi


APP_OLLAMA_HOST: str = os.environ.get("APP_OLLAMA_HOST", "")
if not APP_OLLAMA_HOST:
    raise Exception("APP_OLLAMA_HOST environment variable not set")

OLLAMA_MODEL = "mistral-openorca"


@dataclass
class ChatRequest:
    msg: str


bp = Blueprint("chat")


@bp.route("/chat", methods={"POST"})
@openapi.definition(
    body={"application/json": ChatRequest},
    summary="Generate text from a prompt msg",
    response=openapi.response(
        200, {"text/plain": str}, "Returns chunked chat completion text"
    ),
)
async def chat(request: Request):
    generate_url = f"http://{APP_OLLAMA_HOST}/api/generate"
    data = json.loads(request.body.decode("utf-8"))
    msg = data.get("msg")
    if not msg:
        logger.error(f"{msg=} not provided in {data=} {request.body=}")
        return text_response("error: msg not provided", status=400)
    generate_request = {
        "model": OLLAMA_MODEL,
        "prompt": msg,
        "stream": True,
    }
    logger.info(f"handling {generate_request=}")
    sanic_response = await request.respond(content_type="text/plain")
    complete_text = ""
    async with aiohttp.ClientSession() as session:
        async with session.post(generate_url, json=generate_request) as response:
            logger.info(f"{response.status=} from {generate_url=}")
            response.raise_for_status()
            async for data in response.content.iter_any():
                data_str = data.decode("utf-8")
                data_obj = json.loads(data_str)
                response_text = data_obj["response"]
                complete_text += response_text
                await sanic_response.send(response_text)
    await sanic_response.eof()
    logger.info(f"handled {generate_request=} with {complete_text=}")
