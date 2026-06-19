# 0587 — Read an attribute

Uses Python's **BeautifulSoup** (`bs4`) with the stdlib `html.parser` to parse a
fixed HTML document. The CSS selector `a` (via `select_one`) finds the anchor
element, and `link["href"]` reads its `href` attribute, printing
`https://example.com`.

## Run

    python3 main.py
