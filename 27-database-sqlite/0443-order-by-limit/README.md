# 0443 — Order by & limit

Inserts six scores into an in-memory SQLite table, then runs `select value from scores order by value desc limit 3` to sort descending and take the top three rows, printing each value on its own line. Uses Python's stdlib `sqlite3` driver with an `:memory:` connection and `executemany` for bulk inserts.

## Run

    python3 main.py
