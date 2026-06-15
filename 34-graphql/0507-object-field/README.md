# 0507 — Object field

Define a GraphQL schema with the strawberry-graphql library and execute a query that returns an object type. The `Query.user` resolver returns a `User` object, and the query selects its `name` field. `strawberry.Schema(...).execute_sync("{ user { name } }")` runs in-process with no HTTP server; the printed value is read from the resolved `result.data["user"]["name"]`.

## Run

    python3 main.py
