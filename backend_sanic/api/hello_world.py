from sanic.response import json
from sanic import Blueprint


bp = Blueprint("hello_world")


@bp.route("/hello_world")
async def hello_world(request):
    return json({"msg": "Hello World"})
