# 0420 — Retry On Error

Implement retry(n) that resubscribes to the source on error up to n times; the source succeeds on the 3rd subscription. A nonlocal counter in a single-element list tracks subscription count, and the error handler resubscribes by re-invoking a closure.

## Run

    python3 main.py
