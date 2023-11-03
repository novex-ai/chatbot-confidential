#!/bin/sh

echo "upgrading alembic database schema"
alembic upgrade head

echo "starting sanic server"
sanic server:app --host=0.0.0.0 --port=8000 --fast
