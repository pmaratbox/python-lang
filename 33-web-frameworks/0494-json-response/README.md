# 0494 — JSON response

Serve a JSON body with the FastAPI framework. The `GET /user` route returns a Python `dict`, which FastAPI serializes to a compact JSON response. The route is exercised in-process via `fastapi.testclient.TestClient` (no fixed port), and `r.text` prints the actual response body `{"name":"alice"}`.

## Run

    python3 main.py
