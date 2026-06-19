# 0616 — Response status code

Uses Python's `httpx` client against an in-process WSGI server via `httpx.WSGITransport` (no socket, no port). The tiny WSGI app exposes only `GET /hello` returning `200 OK`; the client issues the request and prints the integer `status_code` from the response.

## Run

    python3 main.py
