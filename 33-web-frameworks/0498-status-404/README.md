# 0498 — 404 status

Request an undefined route with the FastAPI library. Only `GET /` is defined, so requesting `GET /missing` makes FastAPI return a `404 Not Found`. The route is exercised entirely in-process with FastAPI's `TestClient`, which drives the ASGI app without binding a network port; the printed value is the actual `response.status_code` returned by the framework.

## Run

    python3 main.py
