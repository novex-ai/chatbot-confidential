import os
from sqlalchemy import create_engine
from sqlalchemy.sql import text

APP_POSTGRES_HOST = os.environ.get("APP_POSTGRES_HOST", "localhost")
APP_POSTGRES_USER = os.environ.get("APP_POSTGRES_USER", "postgres")
APP_POSTGRES_PASSWORD = os.environ.get("APP_POSTGRES_PASSWORD", "not_so_secret")
APP_POSTGRES_DB = os.environ.get("APP_POSTGRES_DB", "postgres")

connection_url = (
    f"postgresql+psycopg2://{APP_POSTGRES_USER}:{APP_POSTGRES_PASSWORD}"
    f"@{APP_POSTGRES_HOST}/{APP_POSTGRES_DB}"
)

engine = create_engine(connection_url)


def app():
    with engine.connect() as conn:
        stmt = text("select * from pg_database")
        print(conn.execute(stmt).fetchall())


if __name__ == "__main__":
    app()
