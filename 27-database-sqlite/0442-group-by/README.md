# 0442 — Group by

Aggregate amounts per group: create an in-memory `sales` table, insert rows for two categories, then run `select category,sum(amount) ... group by category order by category` to total each category and print every result as `category sum`. Uses Python's stdlib `sqlite3` driver with `executemany` for binding and a cursor iterator for rows.

## Run

    python3 main.py
