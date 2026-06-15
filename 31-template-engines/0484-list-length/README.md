# 0484 — List length

Render the size of a list with the jinja2 template engine. The template `{{ items | length }}` pipes the `items` list through jinja2's built-in `length` filter, which returns the number of elements. With fixed data `items=[1, 2, 3]` the engine parses and renders the template to the count `3`.

## Run

    python3 main.py
