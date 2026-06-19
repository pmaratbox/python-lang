# 0624 — PUT request

This lesson uses the **httpx** HTTP client against an **in-process WSGI server** (via `httpx.WSGITransport`, so no socket or port is opened). The tiny WSGI app exposes only `PUT /item`, which returns the text `updated`. The client makes a PUT request and prints the response body.

## Run

    python3 main.py
