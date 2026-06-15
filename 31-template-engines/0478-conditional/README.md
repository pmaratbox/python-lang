# 0478 — Conditional

Render with a condition using the Jinja2 template engine. The `{% if %}…{% else %}…{% endif %}` block tests the `logged_in` variable: when it is true the template emits `welcome`, otherwise `guest`. The template is parsed by `jinja2.Template` and rendered with the fixed data `logged_in=True`, so the engine itself picks the branch.

## Run

    python3 main.py
