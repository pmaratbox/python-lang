# 0603 — Inline code

Uses Python's `markdown` library (Python-Markdown) to render a backtick-wrapped inline code span (`` `code` ``) to HTML, then strips the trailing newline the renderer appends, yielding `<p><code>code</code></p>`.

## Run

    python3 main.py
