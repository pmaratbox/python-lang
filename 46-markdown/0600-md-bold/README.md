# 0600 — Bold

Uses Python's `markdown` library (Python-Markdown) to render the inline emphasis `**bold**` to HTML, producing a `<strong>` element wrapped in a paragraph. The library appends a trailing newline, so it is stripped with `.rstrip("\n")` before printing.

## Run

    python3 main.py
