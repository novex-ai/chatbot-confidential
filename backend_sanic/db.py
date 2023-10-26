from contextvars import ContextVar
import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text


APP_POSTGRES_HOST = os.environ.get("APP_POSTGRES_HOST", "localhost")
APP_POSTGRES_USER = os.environ.get("APP_POSTGRES_USER", "postgres")
APP_POSTGRES_PASSWORD = os.environ.get("APP_POSTGRES_PASSWORD", "")
APP_POSTGRES_DB = os.environ.get("APP_POSTGRES_DB", "postgres")

connection_url = (
    f"postgresql+asyncpg://{APP_POSTGRES_USER}:{APP_POSTGRES_PASSWORD}"
    f"@{APP_POSTGRES_HOST}/{APP_POSTGRES_DB}"
)

async_engine = create_async_engine(connection_url, echo=True)

_sessionmaker = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)  # type: ignore

_base_model_session_ctx = ContextVar("session")  # type: ignore


async def execute_sql(sql: str):
    async with _sessionmaker() as session:
        async with session.begin():
            await session.execute(text(sql))


async def inject_sqlalchemy_session(request):
    request.ctx.session = _sessionmaker()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


async def close_sqlalchemy_session(request):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()
