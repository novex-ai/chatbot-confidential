from sanic import Sanic
from backend_sanic.api import bp as api_bp

app = Sanic("app")
app.blueprint(api_bp)

app.static("", "frontend_vue/dist/", index="index.html")
