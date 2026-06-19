# 0583 — Select by tag

Uses Python's `beautifulsoup4` library (with the stdlib `html.parser`) to parse a
fixed HTML document. The CSS type selector `h1` is passed to `select_one` to find
the first `<h1>` element, and `get_text()` returns its text content.

## Run

    python3 main.py
