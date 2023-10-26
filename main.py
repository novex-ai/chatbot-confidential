import asyncio
from contextlib import asynccontextmanager
import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

APP_POSTGRES_HOST = os.environ.get("APP_POSTGRES_HOST", "localhost")
APP_POSTGRES_USER = os.environ.get("APP_POSTGRES_USER", "postgres")
APP_POSTGRES_PASSWORD = os.environ.get("APP_POSTGRES_PASSWORD", "not_so_secret")
APP_POSTGRES_DB = os.environ.get("APP_POSTGRES_DB", "postgres")

connection_url = (
    f"postgresql+asyncpg://{APP_POSTGRES_USER}:{APP_POSTGRES_PASSWORD}"
    f"@{APP_POSTGRES_HOST}/{APP_POSTGRES_DB}"
)

engine = create_async_engine(connection_url, echo=True, future=True)


def async_session_generator(engine):
    return sessionmaker(engine, class_=AsyncSession)


@asynccontextmanager
async def get_session(engine):
    try:
        async_session = async_session_generator(engine)

        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()


async def app():
    async with get_session(engine) as session:
        async with session.begin():
            stmt = text("select * from pg_database")
            result = await session.execute(stmt)
            print(f"{result=}")
            rows = result.fetchall()
            for row in rows:
                print(row)


if __name__ == "__main__":
    asyncio.run(app())
