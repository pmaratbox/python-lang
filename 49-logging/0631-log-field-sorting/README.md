# 0631 — Deterministic field order

Uses the real `structlog` structured-logging library to emit one INFO record `metric` carrying two fields supplied in non-alphabetical order (`zeta=2` then `alpha=1`). The record is rendered as JSON by `structlog.processors.JSONRenderer` and captured in-memory via a `PrintLoggerFactory` writing to a `StringIO` buffer (no real timestamp). We then `json.loads` the captured line and print the normalized form, sorting the structured fields by key so the output is deterministic regardless of insertion order.

## Run

    python3 main.py
