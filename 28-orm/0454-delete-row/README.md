# 0454 — Delete a row

Remove a persisted entity through SQLAlchemy 2.0's ORM. Defines a `User` model with `DeclarativeBase`/`Mapped`/`mapped_column`, creates the schema in an in-memory SQLite database via `Base.metadata.create_all`, and inserts three rows with `Session.add_all`. It loads the entity with `Session.get(User, 1)`, removes it via `Session.delete`, commits, then reads the remaining rows with `select(User).order_by(User.id)` and prints each name.

## Run

    python3 main.py
