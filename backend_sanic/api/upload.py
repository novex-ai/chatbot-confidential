import os
from pathlib import Path

from sanic import Blueprint, Request
from sanic.log import logger
from sanic.response import json

from backend_sanic.file import make_stored_filename
from backend_sanic.models import FileUpload


APP_DATA_PATH: str = os.environ.get("APP_DATA_PATH", "")
if not APP_DATA_PATH:
    raise Exception("APP_DATA_PATH environment variable not set")

bp = Blueprint("upload")


@bp.route("/upload", methods={"POST"})
async def upload(request: Request):
    file = None
    for _, files in request.files.items():
        # https://sanic.readthedocs.io/en/stable/sanic/api/core.html#sanic.request.File
        file = files[0]
    if file is None:
        return json({"status": "ERROR", "message": "no file uploaded"})
    raw_filename = file.name
    body_bytes = file.body
    size_bytes = len(body_bytes)
    stored_path = store_file(raw_filename, body_bytes)
    logger.info(f"wrote uploaded file to {stored_path=}")
    session = request.ctx.session
    async with session.begin():
        file_upload = FileUpload(
            raw_filename=file.name,
            stored_filename=stored_path.name,
            size_bytes=size_bytes,
        )
        session.add(file_upload)
    #
    return json({"status": "OK"})


def store_file(raw_filename: str, body_bytes: bytes) -> Path:
    stored_filename = make_stored_filename(raw_filename)
    stored_path = Path(APP_DATA_PATH, stored_filename)
    with stored_path.open("wb") as f:
        f.write(body_bytes)
    return stored_path
