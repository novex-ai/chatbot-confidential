from sanic import Sanic
from sanic_ext import Extend
from .api import bp as api_bp
from .db import execute_sql, inject_sqlalchemy_session, close_sqlalchemy_session

app = Sanic("app")
app.config.CORS_ORIGINS = ["http://localhost:9000"]
Extend(app)


@app.listener("before_server_start")
async def setup_pgvector(*_):
    await execute_sql("CREATE EXTENSION IF NOT EXISTS vector")


@app.middleware("request")
async def inject_session(request):
    await inject_sqlalchemy_session(request)


@app.middleware("response")
async def close_session(request, response):
    await close_sqlalchemy_session(request)


app.blueprint(api_bp, url_prefix="/api")
app.static("", "frontend_quasar_vue/dist/spa/", index="index.html")
