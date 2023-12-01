import json

from sanic.log import logger

from backend_sanic.api_generate import generate_text


async def pipe_generated_response(prompt_msg: str, sanic_response):
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
    return complete_text
