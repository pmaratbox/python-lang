# 0439 — Parameterized query

Creates an in-memory SQLite table of users, inserts three rows, then runs `select name from users where id=?` with the value `2` supplied through a real bound parameter (never string interpolation). Uses Python's stdlib `sqlite3` driver, passing the parameter tuple to `Connection.execute` and reading the result with `fetchone`.

## Run

    python3 main.py
