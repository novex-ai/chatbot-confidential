from sanic import Blueprint
from .chat import bp as chat_bp
from .file_uploads import bp as file_uploads_bp
from .initial_chat import bp as initial_chat_bp
from .hello_world import bp as hello_world_bp
from .upload import bp as upload_bp

bp = Blueprint.group(
    chat_bp, file_uploads_bp, initial_chat_bp, hello_world_bp, upload_bp
)
