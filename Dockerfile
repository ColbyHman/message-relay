FROM python:3.13-slim-bookworm

WORKDIR /app

COPY requirements.txt /app
COPY src/ /app/src/

RUN ls -l /app/src/

RUN python3 -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

CMD ["python3", "-u", "-m", "message_relay.main"]