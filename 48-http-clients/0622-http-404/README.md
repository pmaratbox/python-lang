# 0622 — Handle 404

This lesson uses the **httpx** HTTP client against an **in-process WSGI server** (`httpx.WSGITransport`, no socket and no port). The server defines no routes, so a request to `/missing` falls through to a `404 Not Found` response. The client reads the integer status code from that response.

## Run

    python3 main.py
