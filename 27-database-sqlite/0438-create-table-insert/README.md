# 0438 — Create table & insert

Creates a `users(id integer, name text)` table in an in-memory SQLite database, inserts three rows with `executemany`, then selects the names back ordered by id and prints each on its own line. Uses Python's stdlib `sqlite3` driver with parameterized `insert` statements.

## Run

    python3 main.py
