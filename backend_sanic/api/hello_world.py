from sanic.response import json
from sanic import Blueprint


bp = Blueprint("hello_world", url_prefix="/hello_world")


@bp.route("/")
async def hello_world(request):
    return json({"msg": "Hello World"})
