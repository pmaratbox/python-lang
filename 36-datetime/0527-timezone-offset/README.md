# 0527 — Timezone offset

Use the `pendulum` date/time library to parse a fixed UTC instant (`2026-06-15T12:00:00Z`, never the current time) with `pendulum.parse(...)`, then convert it to a fixed `+05:00` offset via `.in_timezone(pendulum.FixedTimezone(5 * 3600))` — a fixed-offset zone that does not depend on the OS timezone database. The resulting local hour (`17`) is computed by the library, not hardcoded.

## Run

    python3 main.py
