FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update \
    && apt-get install --no-install-recommends git ffmpeg libsm6 libxext6 make -y \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml  /app/pyproject.toml
COPY Makefile /app/Makefile

RUN pip install --upgrade pip setuptools wheel \
    && make lock \
    && pip install -r /app/requirements.txt \
    && pip cache purge \
    && rm -rf /root/.cache/pip

# copy project
COPY app /app/app

CMD uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8080