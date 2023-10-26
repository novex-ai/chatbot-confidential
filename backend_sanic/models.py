from sqlalchemy import DateTime, String, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class FileUpload(Base):
    __tablename__ = "file_upload"

    id: Mapped[int] = mapped_column(primary_key=True)
    uploaded_at = mapped_column(DateTime, default=func.now(), nullable=False)
    status = mapped_column(String, server_default="UPLOADED", nullable=False)
    raw_filename = mapped_column(String, nullable=False)
    stored_filename = mapped_column(String, nullable=False)
    size_bytes = mapped_column(Integer, nullable=False)


metadata = Base.metadata
