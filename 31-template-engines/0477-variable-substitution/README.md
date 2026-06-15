# 0477 — Variable substitution

Render a template with the Jinja2 engine. The template `Hello {{ name }}` uses Jinja2's variable substitution syntax: the `{{ name }}` expression is replaced at render time with the value passed to `Template.render(name="alice")`, producing `Hello alice`.

## Run

    python3 main.py
