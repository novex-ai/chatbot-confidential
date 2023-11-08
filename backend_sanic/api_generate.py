from contextlib import asynccontextmanager
import os
import socket

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
    logger.info(f"generate text {generate_url=} {prompt_msg=}")
    async with _make_docker_safe_aiohttp_session() as session:
        response = await session.post(generate_url, json=generate_request)
        logger.info(f"{response.status=} from {generate_url=} {response.content=}")
        yield response


async def pull_llm_model() -> bool:
    pull_url = f"http://{APP_OLLAMA_HOST}/api/pull"
    pull_request = {
        "name": OLLAMA_MODEL,
    }
    logger.info(f"pulling LLM from ollama.ai {pull_url=}")
    try:
        async with _make_docker_safe_aiohttp_session() as session:
            async with session.post(pull_url, json=pull_request) as response:
                response_data = await response.text()
                logger.info(f"{response.status=} from {pull_url=} {response_data=}")
                return response.status == 200
    except aiohttp.client_exceptions.ClientConnectorError:
        msg = "ERROR: ollama.ai is not running - please DOWNLOAD AND INSTALL https://ollama.ai/download"
        logger.error(msg)
        return False


@asynccontextmanager
async def _make_docker_safe_aiohttp_session():
    session = aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            family=socket.AF_INET, verify_ssl=False, use_dns_cache=False
        )
    )
    try:
        yield session
    finally:
        await session.close()
