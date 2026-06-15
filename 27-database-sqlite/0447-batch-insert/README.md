# 0447 — Batch insert

Insert many rows efficiently in one transaction. Uses Python's standard-library `sqlite3` driver: `executemany` binds a prepared `insert into t values(?)` statement against 1000 rows (values 1..1000), and the `with conn:` block wraps the whole batch in a single committed transaction. A final `select count(*) from t` confirms 1000 rows were inserted.

## Run

    python3 main.py
