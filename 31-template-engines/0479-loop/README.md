# 0479 — Loop

Iterate a list inside a template with jinja2. The `{% for n in nums %}...{% endfor %}` block statement repeats its body once per element of the `nums` list passed to `render`, emitting each number followed by a newline. The trailing newline is trimmed before printing so the output is `1\n2\n3`.

## Run

    python3 main.py
