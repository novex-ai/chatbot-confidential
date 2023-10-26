#!/bin/sh

alembic upgrade head

python run_server.py
