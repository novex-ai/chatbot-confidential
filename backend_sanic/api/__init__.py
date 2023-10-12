from sanic import Blueprint
from .hello_world import bp as hello_world_bp

bp = Blueprint.group(hello_world_bp, url_prefix="/api")
