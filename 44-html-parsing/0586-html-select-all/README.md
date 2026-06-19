# 0586 — Select all matching

This lesson uses Python's **BeautifulSoup** (`bs4`) HTML-parsing library with the stdlib `html.parser`. It selects ALL elements with class `item` via the CSS selector `.item` (using `soup.select(".item")`), extracts each element's text with `get_text()`, and joins the results with commas.

## Run

    python3 main.py
