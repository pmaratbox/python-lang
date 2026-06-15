# 0496 — Query parameter

Read a query-string parameter with the FastAPI library. The `@app.get("/greet")` handler declares a `name: str` argument, which FastAPI binds to the `?name=` query parameter, and returns `hello ` + the name via a `PlainTextResponse` (so FastAPI does not JSON-wrap the string). The route is exercised entirely in-process with FastAPI's `TestClient`, which drives the ASGI app without binding a network port; the printed value is the actual response body (`response.text`).

## Run

    python3 main.py
