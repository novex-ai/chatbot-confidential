import os

from sanic import Blueprint, Request, Websocket


APP_OLLAMA_HOST: str = os.environ.get("APP_OLLAMA_HOST", "")
if not APP_OLLAMA_HOST:
    raise Exception("APP_OLLAMA_HOST environment variable not set")

bp = Blueprint("chat")


@bp.websocket("/chat")
async def chat(request: Request, ws: Websocket):
    pass
