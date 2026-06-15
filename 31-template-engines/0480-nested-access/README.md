# 0480 — Nested access

Uses the Jinja2 template engine's dotted attribute access (`{{ user.name }}`) to reach a nested field inside a dictionary; Jinja2 resolves the dot first as an attribute and then as a dictionary key.

## Run

    python3 main.py
