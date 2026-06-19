# 0617 — Parse JSON response

Uses the real `httpx` client against an in-process WSGI server via `httpx.WSGITransport` (no socket, no port). The tiny WSGI app serves `GET /user` as JSON `{"name":"Alice","age":30}`; the client fetches it, calls `.json()` to parse the body, and prints the `name` field.

## Run

    python3 main.py
