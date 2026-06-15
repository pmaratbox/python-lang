# 0500 — Request header

Read a request header with the FastAPI library. The `@app.get("/whoami")` handler declares an `x_name: str = Header()` argument, which FastAPI binds to the `X-Name` request header (underscores in the parameter name map to hyphens), and echoes its value back via a `PlainTextResponse` (so FastAPI does not JSON-wrap the string). The route is exercised entirely in-process with FastAPI's `TestClient`, which drives the ASGI app without binding a network port; the printed value is the actual response body (`response.text`).

## Run

    python3 main.py
