# 0495 — Path parameter

Use the FastAPI web framework. The route `GET /users/{id}` declares a path parameter `id`; the handler echoes it back as plain text via `PlainTextResponse`. The route is exercised in-process with FastAPI's `TestClient` (no fixed port is bound) by requesting `/users/42`, and the captured response body `42` is printed.

## Run

    python3 main.py
