# 0497 — POST JSON body

Parse a JSON request body with the FastAPI framework. The `POST /sum` route declares a Pydantic model parameter, so FastAPI parses and validates the JSON body `{"a":2,"b":3}` into typed fields; the handler returns their sum as plain text. The route is exercised in-process via `fastapi.testclient.TestClient` (no fixed port), and `r.text` prints the actual response body `5`.

## Run

    python3 main.py
