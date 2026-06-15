# 0493 — Hello route

Define a GET route with the FastAPI library. The `@app.get("/")` handler returns the text `hello` via a `PlainTextResponse` (so FastAPI does not JSON-wrap the string). The route is exercised entirely in-process with FastAPI's `TestClient`, which drives the ASGI app without binding a network port; the printed value is the actual response body (`response.text`).

## Run

    python3 main.py
