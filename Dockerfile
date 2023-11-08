FROM python:3.11-bookworm

WORKDIR /sanic

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY models/ models/
COPY ["alembic.ini", "server.py", "run_entrypoint.sh", "./"]
COPY alembic/ alembic/
COPY backend_sanic/ backend_sanic/
COPY frontend_quasar_vue/dist/ frontend_quasar_vue/dist/

EXPOSE 8000

CMD ["bash", "run_entrypoint.sh"]
