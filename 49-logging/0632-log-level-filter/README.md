# 0632 — Level filtering

Uses the **structlog** library with a filtering bound logger whose minimum level is `WARNING`. An INFO record `hidden` is emitted but suppressed, then a WARN record `visible` is emitted and captured. Records are rendered as JSON to an in-memory `StringIO` sink (no timestamp), parsed back, and printed as a normalized `level|message` line (`warning` mapped to `warn`).

## Run

    python3 main.py
