# 0481 — Loop over objects

Render with jinja2's `{% for %}` block, iterating a list of dictionaries and accessing each object's fields via dot notation. The template loops over `users`, emitting `name: age` per line, and jinja2 resolves `u.name` and `u.age` against each dict in turn.

## Run

    python3 main.py
