from dataclasses import dataclass
from typing import List

from sanic import Blueprint, Request
from sanic.log import logger
from sanic.response import json as json_response
from sanic_ext import openapi
from sqlalchemy import func, select

from backend_sanic.models import FileUpload, EmbeddedChunk


@dataclass
class FileUploadsResponse:
    file_uploads: List[FileUpload]


bp = Blueprint("file_uploads")


@bp.route("/file_uploads", methods={"GET"})
@openapi.definition(
    response=openapi.response(
        200, FileUploadsResponse, "Returns chunked chat completion text"
    ),
)
async def get_file_uploads(request: Request):
    """Get all file uploads"""
    session = request.ctx.session
    async with session.begin():
        result = await session.execute(
            select(FileUpload, func.count(EmbeddedChunk.id).label("num_chunks"))
            .join(EmbeddedChunk, FileUpload.id == EmbeddedChunk.file_upload_id)
            .group_by(FileUpload.id)
            .order_by(FileUpload.uploaded_at.desc())
        )
        rows = result.all()
    file_uploads = []
    for row in rows:
        file_upload_obj, num_chunks = row
        file_upload = file_upload_obj.to_dict()
        file_upload["num_chunks"] = num_chunks
        file_uploads.append(file_upload)
    logger.info(f"{file_uploads=}")
    return json_response(
        {
            "file_uploads": file_uploads,
        }
    )
