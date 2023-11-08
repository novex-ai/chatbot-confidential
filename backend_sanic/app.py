import sys

from sanic import Sanic
from sanic_ext import Extend
from .api import bp as api_bp
from .api_generate import pull_llm_model
from .db import inject_sqlalchemy_session, close_sqlalchemy_session
from .embeddings import get_embedding_model

app = Sanic("app")
app.config.CORS_ORIGINS = ["http://localhost:9000"]
Extend(app)


@app.main_process_start
async def main_process_start(app):
    """
    Ensure that ollama.ai has pulled our model before we start serving requests
    """
    success = await pull_llm_model()
    if not success:
        sys.exit(1)


@app.before_server_start
async def before_server_start(app):
    """
    ensure that each worker is ready to serve requests
    https://sanic.dev/en/guide/basics/listeners.html
    """
    model = get_embedding_model()
    assert model is not None


@app.middleware("request")
async def inject_session(request):
    await inject_sqlalchemy_session(request)


@app.middleware("response")
async def close_session(request, response):
    await close_sqlalchemy_session(request)


app.blueprint(api_bp, url_prefix="/api")
app.static("", "frontend_quasar_vue/dist/spa/", index="index.html")
