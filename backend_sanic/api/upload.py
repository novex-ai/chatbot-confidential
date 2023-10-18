import os
from pathlib import Path

from sanic import Blueprint
from sanic.log import logger
from sanic.response import json


APP_DATA_PATH = os.environ.get("APP_DATA_PATH")
if not APP_DATA_PATH:
    raise Exception("APP_DATA_PATH environment variable not set")

bp = Blueprint("upload")


@bp.route("/upload", methods={"POST"})
async def upload(request):
    for filename, files in request.files.items():
        # https://sanic.readthedocs.io/en/stable/sanic/api/core.html#sanic.request.File
        file = files[0]

        logger.info(repr(filename))
        logger.info(f"{file=} {type(file)=}")
    return json({"msg": "OK"})
