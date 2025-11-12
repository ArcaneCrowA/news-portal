FROM python:3.10.18-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml /app

RUN uv sync

COPY . /app

ENV PYTHONPATH=/app

EXPOSE 80

CMD ["uv", "run", "fastapi", "run", "app/main.py"]