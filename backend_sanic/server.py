from sanic import Sanic
from .api import bp as api_bp

app = Sanic("app")
app.blueprint(api_bp)
