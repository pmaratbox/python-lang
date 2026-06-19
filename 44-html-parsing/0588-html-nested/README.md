# 0588 — Descendant selector

Parses a fixed HTML document with the `beautifulsoup4` library (using the stdlib `html.parser`) and queries it with the CSS descendant selector `.content p`, which matches every `<p>` nested anywhere inside the `.content` element. Each matched paragraph's text is extracted with `get_text()` and joined with commas to print `first,second`.

## Run

    python3 main.py
