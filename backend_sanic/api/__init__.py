from sanic import Blueprint
from .chat import bp as chat_bp
from .hello_world import bp as hello_world_bp
from .upload import bp as upload_bp

bp = Blueprint.group(chat_bp, hello_world_bp, upload_bp)
