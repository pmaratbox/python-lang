# 0524 — Date components

Use the pendulum library to parse a FIXED instant (`2026-06-15T00:00:00+00:00`, a fixed UTC offset — never the current time) and extract its calendar components. The `.year`, `.month`, and `.day` accessors are computed by pendulum from the parsed instant, and each is printed on its own line.

## Run

    python3 main.py
