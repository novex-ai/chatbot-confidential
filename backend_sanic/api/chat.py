from sanic import Blueprint, Request, Websocket


bp = Blueprint("chat")


@bp.websocket("/chat")
async def chat(request: Request, ws: Websocket):
    pass
