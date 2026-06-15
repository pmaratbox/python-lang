# 0440 — Update & delete

Modify and remove rows, then read the result. Creates an in-memory `users` table, inserts three rows, runs an `update` to rename the row with id 2 and a `delete` to remove the row with id 1, then selects the remaining rows ordered by id. Uses Python's stdlib `sqlite3` driver with parameterized `executemany` inserts and real SQL DML statements.

## Run

    python3 main.py
