# 0483 — Default value

This lesson uses jinja2, Python's real template engine, with its `default` filter to supply a fallback. The template `{{ name | default('anonymous') }}` is rendered with no data for `name`, so the filter substitutes `anonymous` for the undefined variable.

## Run

    python3 main.py
