# 0445 — Transactions

Create a table `t` in an in-memory SQLite database, then exercise real transaction control: one transaction inserts 1 and 2 and `COMMIT`s, while a second transaction inserts 3 and `ROLLBACK`s, so the rolled-back row never persists. A final `select n from t order by n` prints only 1 and 2. Uses Python's stdlib `sqlite3` driver with `isolation_level = None` for explicit `begin`/`commit`/`rollback`.

## Run

    python3 main.py
