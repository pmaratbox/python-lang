# 0521 — Parse & format

Use the `pendulum` date/time library to parse a fixed ISO date string (`2026-06-15`, never the current time) into a datetime object with `pendulum.parse(...)`, then format it back to ISO (`YYYY-MM-DD`) via `.format(...)`. The round-tripped value is computed by the library, not hardcoded.

## Run

    python3 main.py
