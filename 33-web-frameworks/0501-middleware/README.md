# 0501 — Middleware

Register an HTTP middleware with the FastAPI library using `@app.middleware("http")`. The middleware awaits the downstream handler, drains the streamed response body, and prefixes it with `[mw] ` before returning a new `PlainTextResponse`; the route handler itself only returns `hello`, so the prefix is added entirely by the middleware. The route is exercised in-process with FastAPI's `TestClient` (which drives the ASGI app without binding a network port), and the printed value is the actual transformed response body (`response.text`).

## Run

    python3 main.py
