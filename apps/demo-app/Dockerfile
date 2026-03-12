FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace

# Copy local workspace packages required by demo-app.
COPY pkgs/converters ./pkgs/converters
COPY pkgs/quotes ./pkgs/quotes
COPY apps/demo-app ./apps/demo-app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ./pkgs/converters ./pkgs/quotes \
    && pip install --no-cache-dir --no-deps ./apps/demo-app

WORKDIR /workspace/apps/demo-app

CMD ["python", "-m", "demo_app.main"]
