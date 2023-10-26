from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


# class FileUpload(Base):
#    __tablename__ = "file_upload"
#
#    id: Mapped[int] = mapped_column(primary_key=True)
#    uploaded_at = Column(DateTime, default=func.now(), nullable=False)
#    status = Column(String, server_default="UPLOADED", nullable=False)
#    raw_filename = Column(String, nullable=False)
#    stored_filename = Column(String, nullable=False)
#    size_bytes = Column(Integer, nullable=False)


metadata = Base.metadata
