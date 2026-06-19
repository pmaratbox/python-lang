# 0628 — Log a string field

Uses the real `structlog` structured-logging library to emit an INFO record `login` with one structured string field `user=alice`. structlog is configured to render each record as JSON via a `PrintLoggerFactory` writing to an in-memory `StringIO` buffer (no real timestamp processor), so the record is captured in memory. The captured JSON line is then parsed and printed as a normalized `level|message|key=value` line with fields sorted by key.

## Run

    python3 main.py
