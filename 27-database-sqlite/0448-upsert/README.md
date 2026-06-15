# 0448 — Upsert

Insert or update on a primary-key conflict. Creates an in-memory `inv` table keyed by `item`, inserts `apple` with quantity 5, then upserts `apple` again using `insert ... on conflict(item) do update set qty=qty+excluded.qty` (so apple becomes 10), and upserts `banana` the same way (which inserts a new row). Finally selects ordered by item and prints each as `item qty`. Uses Python's stdlib `sqlite3` driver against `:memory:`.

## Run

    python3 main.py
