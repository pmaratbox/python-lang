# 0627 — Log at error level

Uses the real `structlog` structured-logging library to emit an ERROR record with the message `boom`. The logger is configured with a `JSONRenderer` writing to an in-memory `StringIO` buffer (via `PrintLoggerFactory`, so no real timestamp and nothing leaks to the console), and the captured JSON line is parsed and printed as the normalized `level|message` form.

## Run

    python3 main.py
