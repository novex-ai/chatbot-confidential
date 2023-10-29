from datetime import datetime
from typing import List

from pgvector.sqlalchemy import Vector  # type: ignore
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .embeddings import EMBEDDING_DIMENSIONS


# see
# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#declarative-table-with-mapped-column


class Base(DeclarativeBase):
    pass


class FileUpload(Base):
    __tablename__ = "file_upload"

    id: Mapped[int] = mapped_column(primary_key=True)
    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), nullable=False
    )
    status: Mapped[str] = mapped_column(
        String, server_default="UPLOADED", nullable=False
    )
    raw_filename: Mapped[str]
    stored_filename: Mapped[str]
    size_bytes: Mapped[int]

    chunks: Mapped[List["EmbeddedChunk"]] = relationship(back_populates="file_upload")


class EmbeddedChunk(Base):
    __tablename__ = "embedded_chunk"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_upload_id: Mapped[int] = mapped_column(
        None, ForeignKey("file_upload.id"), nullable=False
    )
    chunk_index: Mapped[int]
    vector: Mapped[Vector] = mapped_column(Vector(EMBEDDING_DIMENSIONS), nullable=False)
    chunk_text: Mapped[str] = mapped_column(String, nullable=False)

    file_upload: Mapped[FileUpload] = relationship(back_populates="chunks")


metadata = Base.metadata
