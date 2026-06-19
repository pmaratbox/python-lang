# 0629 — Log an integer field

Uses the real `structlog` structured-logging library to emit one INFO record with message `processed` and a single integer field `count=5`. The logger is configured with a `JSONRenderer` writing to an in-memory `StringIO` buffer (via `PrintLoggerFactory`), so there is no real timestamp or console output. Each captured JSON line is parsed with `json.loads`, then normalized to `level|message` followed by each field sorted by key as `|key=value`, with the integer value printed as-is.

## Run

    python3 main.py
