from sanic.log import logger
from sanic.response import json as json_response
from sanic import Blueprint, Request


bp = Blueprint("hello_world")


@bp.route("/hello_world")
async def hello_world(request: Request):
    logger.info("handling hello_world")
    return json_response({"msg": "Hello World"})
