from sanic import Blueprint
from .hello_world import bp as hello_world_bp
from .upload import bp as upload_bp

bp = Blueprint.group(hello_world_bp, upload_bp)
