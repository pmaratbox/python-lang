# 0619 — Query parameters

This lesson uses the **httpx** HTTP client against an **in-process WSGI server**
(`httpx.WSGITransport`, no socket or port). The server exposes a single route
`GET /greet` that reads the `name` query parameter and returns `hi <name>`. The
client sends `params={"name": "Bob"}`, and we print the response body.

## Run

    python3 main.py
