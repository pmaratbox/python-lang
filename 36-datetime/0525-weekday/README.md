# 0525 — Weekday

Use the `pendulum` date/time library to parse a fixed ISO date (`2026-06-15`, never the current time) with `pendulum.parse(...)`, then read its ISO weekday number via `.isoweekday()` (Monday=1 .. Sunday=7). The weekday is computed by the library, not hardcoded.

## Run

    python3 main.py
