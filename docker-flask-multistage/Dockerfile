#############################
# Builder Stage
#############################

FROM python:3.14-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt
#############################
# Final Stage
#############################
FROM python:3.14-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
# Create non-root user
RUN useradd -m appuser
USER appuser
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"
CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]