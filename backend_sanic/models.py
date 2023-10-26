from datetime import datetime

from pgvector.sqlalchemy import Vector  # type: ignore
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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


class EmbeddedChunk(Base):
    __tablename__ = "embedded_chunk"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_upload_id: Mapped[int] = mapped_column(
        None, ForeignKey("file_upload.id"), nullable=False
    )
    chunk_index: Mapped[int]
    vector: Mapped[Vector] = mapped_column(Vector(EMBEDDING_DIMENSIONS), nullable=False)


metadata = Base.metadata
