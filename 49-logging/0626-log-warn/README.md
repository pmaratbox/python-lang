# 0626 — Log at warn level

Uses the real `structlog` structured-logging library to emit a WARNING-level record with the message `low disk`. The logger is configured with a `JSONRenderer` writing to an in-memory `StringIO` buffer (no timestamp processor, so no real time leaks into the output), and each captured JSON line is parsed back with `json.loads`. The level is normalized from `warning` to `warn` and printed as the line `warn|low disk`.

## Run

    python3 main.py
