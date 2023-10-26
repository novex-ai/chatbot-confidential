from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


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


metadata = Base.metadata
