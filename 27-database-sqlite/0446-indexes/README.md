# 0446 — Indexes

Create a `products` table in an in-memory SQLite database, populate it, then execute a `CREATE INDEX` statement on the `sku` column and run a parameterized lookup (`select price ... where sku=?`) bound to `'B'`, printing the matched price. Uses Python's stdlib `sqlite3` driver with `execute`/`executemany` and parameter binding.

## Run

    python3 main.py
