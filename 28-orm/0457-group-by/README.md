# 0457 — Group by

Aggregate per group with SQLAlchemy 2.0's ORM. Defines a `Product` model via `DeclarativeBase`/`Mapped`/`mapped_column`, inserts three rows into an in-memory SQLite database, then runs `select(Product.category, func.sum(Product.price)).group_by(Product.category).order_by(Product.category)` through a `Session`. The grouping and aggregation are expressed entirely with the query-builder API rather than a raw SQL string, and `order_by` makes the output deterministic.

## Run

    python3 main.py
