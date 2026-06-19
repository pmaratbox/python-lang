# 0618 — POST a body

This lesson uses the **httpx** HTTP client against an **in-process WSGI server** (via `httpx.WSGITransport`, so no socket or port is opened). The tiny WSGI app exposes only `POST /echo`, which returns the request body verbatim. The client POSTs the text `ping` and prints the response body.

## Run

    python3 main.py
