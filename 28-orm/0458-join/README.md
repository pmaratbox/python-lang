# 0458 — Join

Join two models with SQLAlchemy 2.0's ORM. Defines `User` and `Post` models via `DeclarativeBase`/`Mapped`/`mapped_column`, with `Post.user_id` declared as a `ForeignKey("users.id")`, then inserts rows into an in-memory SQLite database. The query uses `select(User.name, Post.title).join(Post, Post.user_id == User.id).order_by(User.name, Post.title)` through a `Session` to combine the tables, printing `name title` for each post. The join is expressed with the query-builder API rather than a raw SQL string.

## Run

    python3 main.py
