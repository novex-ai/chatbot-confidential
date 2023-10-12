from sanic.response import text
from sanic import Blueprint


bp = Blueprint("hello_world", url_prefix="/hello_world")


@bp.route("/")
async def hello_world(request):
    return text("Hello, world.")
