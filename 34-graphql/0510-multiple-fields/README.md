# 0510 — Multiple fields

Define a GraphQL schema with the strawberry-graphql library and execute a query in-process that selects multiple fields of an object type. The `User` type exposes `name` and `age`, and `Query.user` resolves to a single user. Executing `{ user { name age } }` with `strawberry.Schema(...).execute_sync(...)` runs the query without any HTTP server; both values are read from the resolved `result.data["user"]` and printed on their own lines.

## Run

    python3 main.py
