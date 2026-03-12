FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /workspace \
    && python -m venv /opt/venv \
    && chown -R appuser:appuser /workspace /opt/venv

WORKDIR /workspace

# Copy local workspace packages required by tryout-app.
COPY --chown=appuser:appuser pkgs/quotes ./pkgs/quotes
COPY --chown=appuser:appuser apps/tryout-app ./apps/tryout-app

USER appuser

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ./pkgs/quotes \
    && pip install --no-cache-dir --no-deps ./apps/tryout-app

WORKDIR /workspace/apps/tryout-app

CMD ["python", "-m", "tryout_app.main"]
