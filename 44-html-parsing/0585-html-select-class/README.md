# 0585 — Select by class

This lesson uses Python's **BeautifulSoup** (`bs4`) library with the stdlib `html.parser` to query a fixed HTML document. It calls `select_one` with the CSS class selector `.item` to find the first element whose `class` attribute includes `item`, then prints its text (`apple`).

## Run

    python3 main.py
