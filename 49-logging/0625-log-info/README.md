# 0625 — Log at info level

Uses `structlog`, Python's structured-logging library, to emit one INFO record with the message `service started` and no structured fields. The logger is configured to render JSON to an in-memory `StringIO` buffer (no timestamp), then each captured line is parsed and printed as a normalized `level|message` line.

## Run

    python3 main.py
