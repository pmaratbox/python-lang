# 0621 — Read a response header

This lesson uses the **httpx** HTTP client against an **in-process WSGI server** (via `httpx.WSGITransport`, so no socket or port is opened). The tiny WSGI app exposes only `GET /info`, which sets a custom response header `X-Count: 7`. The client makes the request and reads `resp.headers["X-Count"]`, printing the value.

## Run

    python3 main.py
