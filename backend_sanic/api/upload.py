import os
from pathlib import Path
from typing import Generator

from docx import Document as DocxDocument  # type: ignore
from pypdf import PdfReader
from sanic import Blueprint, Request
from sanic.log import logger
from sanic.response import json
from sqlalchemy import select

from backend_sanic.api_generate import generate_text
from backend_sanic.db import make_session
from backend_sanic.embeddings import string_to_embeddings
from backend_sanic.file import make_stored_filename
from backend_sanic.models import FileUpload, EmbeddedChunk
from backend_sanic.text import split_text_chunks


UPLOAD_PROCESS_GENERATE_QUESTION = False

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


def split_chunks(stored_path: Path) -> Generator[str, None, None]:
    if not stored_path.is_file():
        raise Exception(f"could not find {stored_path=}")
    file_extension = stored_path.suffix
    if file_extension == ".txt":
        body_bytes = stored_path.read_bytes()
        input = body_bytes.decode("utf-8")
        logger.info(f"reading txt with {len(input)=}")
        for chunk in split_text_chunks(input):
            yield chunk
    elif file_extension == ".pdf":
        pdf_reader = PdfReader(str(stored_path))
        for i, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            logger.info(f"{i=} processing page with {len(page_text)=}")
            if len(page_text) > 1000:
                for chunk in split_text_chunks(page_text):
                    yield chunk
            elif len(page_text) > 0:
                yield page_text
    elif file_extension == ".docx":
        document = DocxDocument(str(stored_path))
        for i, paragraph in enumerate(document.paragraphs):
            paragraph_text = paragraph.text
            logger.info(f"{i=} processing paragraph with {len(paragraph_text)=}")
            if len(paragraph_text) > 1000:
                for chunk in split_text_chunks(paragraph_text):
                    yield chunk
            elif len(paragraph_text) > 0:
                yield paragraph_text
    else:
        raise Exception(f"unknown file extension {file_extension}")


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

    chunk_index = 0
    embedded_chunks = []
    async for chunk_tuple in _generate_chunk_tuples(split_chunks(stored_path)):
        vector, chunk_text = chunk_tuple
        embedded_chunk = EmbeddedChunk(
            chunk_index=chunk_index,
            file_upload_id=file_upload_id,
            vector=vector,
            chunk_text=chunk_text,
        )
        embedded_chunks.append(embedded_chunk)
        chunk_index += 1
    logger.info(f"processed {file_upload_id=} into {len(embedded_chunks)=}")
    async with make_session() as session:
        async with session.begin():
            file_upload = await session.merge(file_upload)
            session.add_all(embedded_chunks)
            file_upload.status = "PROCESSED"
    logger.info(f"processed {file_upload_id=}")


async def _generate_chunk_tuples(chunk_text_generator: Generator[str, None, None]):
    for chunk_text in chunk_text_generator:
        # TODO consider generating multiple questions per chunk
        prompt_msg = f"Generate a standard question that is best answered by the following: {chunk_text}"
        async with generate_text(prompt_msg, stream=False) as response:
            response.raise_for_status()
            data = await response.json()
            question = data["response"]
            logger.debug(f"generated question {question=}")
        question_vector = string_to_embeddings(question)
        logger.info(f"generated {len(question_vector)=} from {question=}")
        yield (question_vector, chunk_text)
        whole_chunk_vector = string_to_embeddings(chunk_text)
        logger.info(f"generated {len(whole_chunk_vector)=} from {len(chunk_text)=}")
        yield (whole_chunk_vector, chunk_text)
