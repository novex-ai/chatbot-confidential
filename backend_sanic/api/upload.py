import os
from pathlib import Path
from typing import List

from sanic import Blueprint, Request
from sanic.log import logger
from sanic.response import json
from sqlalchemy import select

from backend_sanic.db import make_session
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
    session = request.ctx.session
    async with session.begin():
        file_upload = FileUpload(
            raw_filename=raw_filename,
            stored_filename=stored_path.name,
            size_bytes=size_bytes,
            status="QUEUED",
        )
        session.add(file_upload)
    logger.info(
        f"saved file_upload {file_upload.id=} {file_upload.raw_filename=}"
        f" {file_upload.stored_filename=} {file_upload.size_bytes=}"
    )
    request.app.add_task(process_file_upload(file_upload.id))
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


async def process_file_upload(file_upload_id: int):
    logger.info(f"processing {file_upload_id=}")
    async with make_session() as session:
        async with session.begin():
            file_upload = await session.scalar(
                select(FileUpload).where(FileUpload.id == file_upload_id)
            )
            if file_upload is None:
                logger.error(f"could not find {file_upload_id=}")
                return
            logger.info(f"got {file_upload=}")
            file_upload.status = "PROCESSING"
    stored_filename = file_upload.stored_filename
    stored_path = Path(_upload_path, stored_filename)
    text_chunks = split_chunks(stored_path.read_bytes(), stored_path.suffix)
    logger.info(f"split file into {len(text_chunks)=}")
    vectors = []
    for i, chunk_text in enumerate(text_chunks):
        vector = strings_to_embeddings(chunk_text)
        logger.info(f"processed {i=} {len(chunk_text)=} {len(vector)=}")
        vectors.append(vector)
    async with make_session() as session:
        async with session.begin():
            file_upload = await session.merge(file_upload)
            embedded_chunks = []
            for i, (chunk_text, vector) in enumerate(zip(text_chunks, vectors)):
                embedded_chunk = EmbeddedChunk(
                    chunk_index=i,
                    file_upload_id=file_upload.id,
                    vector=vector,
                    chunk_text=chunk_text,
                )
                embedded_chunks.append(embedded_chunk)
            session.add_all(embedded_chunks)
            file_upload.status = "PROCESSED"
    logger.info(f"processed {file_upload_id=}")
