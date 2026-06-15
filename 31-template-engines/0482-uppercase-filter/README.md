# 0482 — Uppercase filter

Render a fixed Jinja2 template that applies the built-in `upper` filter to a variable. In Jinja2, filters are applied with the pipe syntax `{{ name | upper }}`, transforming the `name` value (`alice`) to uppercase at render time. The data is fixed (`name="alice"`), so the output is always `ALICE`.

## Run

    python3 main.py
