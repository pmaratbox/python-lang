# 0419 — Catch Error

Implement catchError that, on an error from the source, switches to a fallback stream. The observer is a small class wrapping next/error/complete callbacks, and catchError simply rewires on_error to subscribe the fallback.

## Run

    python3 main.py
