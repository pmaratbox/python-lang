# 0453 — Update a row

Modify a persisted entity with SQLAlchemy 2.0's ORM. Defines a `User` model via `DeclarativeBase`/`Mapped`/`mapped_column`, inserts three rows into an in-memory SQLite database, then loads bob with `Session.get`, sets his `age` to 40, and commits the change. Finally it runs a `select(User).where(User.age >= 35).order_by(User.id)` query and prints `name age` for the matching rows.

## Run

    python3 main.py
