from sanic.response import json
from sanic import Blueprint, Request


bp = Blueprint("hello_world")


@bp.route("/hello_world")
async def hello_world(request: Request):
    return json({"msg": "Hello World"})
