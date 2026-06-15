# 0504 — Error handler

Handle a thrown error with the FastAPI framework's error handling. The `GET /boom` route raises a `RuntimeError`, and FastAPI's built-in exception handling catches the unhandled error and turns it into an `HTTP 500 Internal Server Error` response. The route is exercised in-process via `fastapi.testclient.TestClient` constructed with `raise_server_exceptions=False` (no fixed port), so the framework produces the real 500 response instead of re-raising; `r.status_code` then prints the actual status code returned by the framework.

## Run

    python3 main.py
