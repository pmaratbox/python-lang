# 0503 — Method routing

Register two handlers on the same path with the FastAPI library: `@app.get("/item")` returns `get` and `@app.post("/item")` returns `post`, each via a `PlainTextResponse` so FastAPI does not JSON-wrap the string. FastAPI routes by HTTP method, so the same path dispatches to a different handler per verb. The route is exercised in-process with FastAPI's `TestClient` (no network port); a `POST /item` is sent and the actual response body is printed.

## Run

    python3 main.py
