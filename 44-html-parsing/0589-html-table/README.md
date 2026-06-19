# 0589 — Extract table cells

Parses a small HTML `<table>` with Python's `beautifulsoup4` library (using the standard-library `html.parser` backend) and queries it with the CSS selector `td` to select every cell. Each cell's text is read with `get_text()` and the values are joined row-major with commas to print `r1c1,r1c2,r2c1,r2c2`.

## Run

    python3 main.py
