# 0528 — Unix timestamp

Use the `pendulum` date/time library to parse a fixed UTC instant (`2026-06-15T00:00:00Z`, never the current time) with `pendulum.parse(...)`, then read its Unix timestamp (epoch seconds) via `.int_timestamp`. The epoch value is computed by the library, not hardcoded.

## Run

    python3 main.py
