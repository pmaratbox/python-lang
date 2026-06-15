# 0505 — Hello query

Define a GraphQL schema with the strawberry-graphql library and execute a simple query in-process. The `Query` type exposes a `hello` field whose resolver returns `world`. `strawberry.Schema(...).execute_sync("{ hello }")` runs the query without any HTTP server; the printed value is read from the resolved `result.data["hello"]`.

## Run

    python3 main.py
