# 0437 — Connect & query

Open an in-memory SQLite database and run a single query. Uses Python's standard-library `sqlite3` driver: `sqlite3.connect(":memory:")` opens the database, `execute` runs the SQL `select 42`, and `fetchone()` retrieves the single integer result that gets printed.

## Run

    python3 main.py
