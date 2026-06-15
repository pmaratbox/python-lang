# 0449 — Define model & insert

Define an entity, insert rows, and read them back using SQLAlchemy 2.0's ORM. A `User` model is declared with `DeclarativeBase`, `Mapped`, and `mapped_column`; `Base.metadata.create_all` builds the schema on an in-memory engine from `create_engine("sqlite://")`. Rows are inserted through a `Session` with `add_all` plus `commit`, then read back with `select(User).order_by(User.id)` via `session.scalars`, printing each name.

## Run

    python3 main.py
