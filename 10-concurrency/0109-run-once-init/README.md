# 0109 — Run-Once Initialization

Ensure an initializer runs exactly once even when several threads race to trigger it, printing `init count: 1`. A lock plus a double-checked `_done` flag implements the run-once guard idiomatically.

## Run

    python3 main.py
