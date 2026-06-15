# 0509 — Nested object

Define a GraphQL schema with the strawberry-graphql library and execute a query that selects a field through nested object types. The `Query.user` resolver returns a `User` whose `address` is an `Address` with `city = "oslo"`. The query `{ user { address { city } } }` runs in-process via `strawberry.Schema(...).execute_sync(...)`, and the printed value is read from the nested `result.data["user"]["address"]["city"]`.

## Run

    python3 main.py
