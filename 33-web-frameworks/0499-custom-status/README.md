# 0499 — Custom status

Return a custom HTTP status code with the FastAPI framework. The `POST /create` route declares `status_code=201`, so a successful request responds with `201 Created` instead of the default `200`. The route is exercised in-process via `fastapi.testclient.TestClient` (no fixed port), and `r.status_code` prints the actual status code returned by the framework.

## Run

    python3 main.py
