# 0615 — GET request

Uses the real `httpx` client library to make a GET request against a tiny in-process WSGI server (mounted via `httpx.WSGITransport`, so no socket or port is opened). The server exposes a single `GET /hello` route returning the text `hello world`, and the client reads that response body.

## Run

    python3 main.py
