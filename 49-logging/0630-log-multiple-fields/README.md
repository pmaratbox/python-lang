# 0630 — Log multiple fields

Uses **structlog** to emit one INFO record `request` carrying two structured fields, `method=GET` (string) and `status=200` (int). The logger is configured with a `JSONRenderer` writing to an in-memory `StringIO` (no timestamp), so each captured JSON line is parsed back with `json.loads`, the level/message keys are stripped, and the remaining fields are printed sorted by key as `|key=value`.

## Run

    python3 main.py
