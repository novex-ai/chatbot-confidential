import os
from pathlib import Path
from typing import List

from sanic import Blueprint, Request
from sanic.log import logger
from sanic.response import json

from backend_sanic.embeddings import strings_to_embeddings
from backend_sanic.file import make_stored_filename
from backend_sanic.models import FileUpload, EmbeddedChunk
from backend_sanic.text import split_text_chunks


APP_DATA_PATH: str = os.environ.get("APP_DATA_PATH", "")
if not APP_DATA_PATH:
    raise Exception("APP_DATA_PATH environment variable not set")

_upload_path = Path(APP_DATA_PATH, "uploads")
_upload_path.mkdir(parents=True, exist_ok=True)

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
    chunks = split_chunks(body_bytes, stored_path.suffix)
    logger.info(f"split uploaded file into {len(chunks)} chunks")
    vectors = strings_to_embeddings(chunks)
    session = request.ctx.session
    async with session.begin():
        embedded_chunks = []
        for i, (chunk_text, vector) in enumerate(zip(chunks, vectors)):
            logger.info(f"{i=} {len(chunk_text)=} {len(vector)=}")
            embedded_chunk = EmbeddedChunk(
                chunk_index=i, vector=vector, chunk_text=chunk_text
            )
            embedded_chunks.append(embedded_chunk)
        file_upload = FileUpload(
            raw_filename=raw_filename,
            stored_filename=stored_path.name,
            size_bytes=size_bytes,
            chunks=embedded_chunks,
        )
        session.add(file_upload)
    return json({"status": "OK"})


def store_file(raw_filename: str, body_bytes: bytes) -> Path:
    stored_filename = make_stored_filename(raw_filename)
    stored_path = Path(_upload_path, stored_filename)
    with stored_path.open("wb") as f:
        f.write(body_bytes)
    return stored_path


def split_chunks(body_bytes: bytes, file_extension: str) -> List[str]:
    if file_extension == ".txt":
        input = body_bytes.decode("utf-8")
        chunks = split_text_chunks(input)
    else:
        raise Exception(f"unknown file extension {file_extension}")
    return chunks
