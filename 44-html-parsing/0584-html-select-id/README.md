# 0584 — Select by id

This lesson uses Python's **BeautifulSoup** (`bs4`) library with the stdlib `html.parser` to query a fixed HTML document. It calls `select_one` with the CSS id selector `#status` to find the element whose `id` attribute is `status`, then prints its text (`active`).

## Run

    python3 main.py
