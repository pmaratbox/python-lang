# 0620 — Send a request header

This lesson uses the [`httpx`](https://www.python-httpx.org/) client to send a custom request header. The server runs in-process via `httpx.WSGITransport` (no socket, no port): a tiny WSGI app exposes only `GET /token`, which echoes the incoming `X-Token` header (read from `environ["HTTP_X_TOKEN"]`) back in the response body. The client sends `X-Token: secret` and prints the body it receives.

## Run

    python3 main.py
