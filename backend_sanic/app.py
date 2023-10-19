from sanic import Sanic
from sanic_ext import Extend
from .api import bp as api_bp

app = Sanic("app")
app.config.CORS_ORIGINS = ["http://localhost:9000"]
Extend(app)

app.blueprint(api_bp, url_prefix="/api")
app.static("", "frontend_quasar_vue/dist/spa/", index="index.html")
