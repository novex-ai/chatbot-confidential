import json
import os

import aiohttp
from sanic import Blueprint, Request
from sanic.response import text as text_response
from sanic.log import logger


APP_OLLAMA_HOST: str = os.environ.get("APP_OLLAMA_HOST", "")
if not APP_OLLAMA_HOST:
    raise Exception("APP_OLLAMA_HOST environment variable not set")

OLLAMA_MODEL = "mistral-openorca"

bp = Blueprint("chat")


logger.info(f"{APP_OLLAMA_HOST=}")


@bp.route("/chat", methods={"POST"})
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
    async with aiohttp.ClientSession() as session:
        async with session.post(generate_url, json=generate_request) as response:
            logger.info(f"{response.status=} from {generate_url=}")
            response.raise_for_status()
            async for data in response.content.iter_any():
                data_str = data.decode("utf-8")
                data_obj = json.loads(data_str)
                response_text = data_obj["response"]
                await sanic_response.send(response_text)
    await sanic_response.eof()
