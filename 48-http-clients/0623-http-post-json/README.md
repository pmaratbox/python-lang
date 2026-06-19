# 0623 — POST JSON, parse JSON

This lesson uses the `httpx` HTTP client against an in-process WSGI app via `httpx.WSGITransport` (no socket, no port). A tiny WSGI server exposes only `POST /double`, which reads JSON `{"x":N}` and returns `{"doubled":2N}`. The client posts `{"x":5}`, parses the JSON reply, and prints the doubled value.

## Run

    python3 main.py
