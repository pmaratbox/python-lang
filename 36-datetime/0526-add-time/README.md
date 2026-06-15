# 0526 — Add time

Parse the fixed instant `2026-06-15T10:00` with the **pendulum** library, then
add 90 minutes using pendulum's duration arithmetic (`.add(minutes=90)`) and
format the result as `HH:mm`. The new time is computed by the library, not
hardcoded.

## Run

    python3 main.py
