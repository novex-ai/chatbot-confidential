from sanic import Sanic
from sanic.response import text

app = Sanic("penned_pachyderm")


@app.get("/")
async def hello_world(request):
    return text("Hello, world." + __name__)
