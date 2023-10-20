import os
from pathlib import Path

from sanic import Blueprint, Request
from sanic.log import logger
from sanic.response import json


APP_DATA_PATH: str = os.environ.get("APP_DATA_PATH", "")
if not APP_DATA_PATH:
    raise Exception("APP_DATA_PATH environment variable not set")

bp = Blueprint("upload")


@bp.route("/upload", methods={"POST"})
async def upload(request: Request):
    for _, files in request.files.items():
        # https://sanic.readthedocs.io/en/stable/sanic/api/core.html#sanic.request.File
        file = files[0]
        path = Path(APP_DATA_PATH, file.name)
        path.write_bytes(file.body)
        logger.info(f"wrote uploaded file to {path=}")
    return json({"status": "OK"})
