from contextlib import asynccontextmanager
import os

import aiohttp
from sanic.log import logger


APP_OLLAMA_HOST: str = os.environ.get("APP_OLLAMA_HOST", "")
if not APP_OLLAMA_HOST:
    raise Exception("APP_OLLAMA_HOST environment variable not set")

OLLAMA_MODEL = "mistral-openorca"


@asynccontextmanager
async def generate_text(prompt_msg: str, stream: bool):
    generate_url = f"http://{APP_OLLAMA_HOST}/api/generate"
    generate_request = {
        "model": OLLAMA_MODEL,
        "prompt": prompt_msg,
        "stream": stream,
    }
    logger.debug(f"generate text {generate_url=} {generate_request=}")
    session = aiohttp.ClientSession()
    try:
        response = await session.post(generate_url, json=generate_request)
        logger.info(f"{response.status=} from {generate_url=}")
        yield response
    finally:
        await session.close()
