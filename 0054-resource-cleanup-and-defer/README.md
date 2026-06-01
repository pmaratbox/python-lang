# 0054 — Resource Cleanup & Defer

Acquire a resource, use it, and let the language release it automatically at scope exit, printing `open`, `use`, and `close` in that order. A `with` block drives the context-manager protocol: `__enter__` runs on entry (printing `open`) and `__exit__` always runs on exit (printing `close`), even if the body raises.

## Run

    python3 main.py
