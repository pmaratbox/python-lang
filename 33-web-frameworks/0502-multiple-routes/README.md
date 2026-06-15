# 0502 — Multiple routes

Register two GET routes with the FastAPI library: `@app.get("/")` returns `home` and `@app.get("/about")` returns `about`, both via `PlainTextResponse` so FastAPI does not JSON-wrap the strings. Both routes are exercised entirely in-process with FastAPI's `TestClient`, which drives the ASGI app without binding a network port; each printed line is the actual response body (`response.text`) for that route.

## Run

    python3 main.py
