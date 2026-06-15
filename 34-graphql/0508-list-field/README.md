# 0508 — List field

Define a GraphQL schema with the strawberry-graphql library and execute a query in-process. The `Query` type exposes a `numbers` field typed as a list of integers (`[Int]`) whose resolver returns `[1, 2, 3]`. `strawberry.Schema(...).execute_sync("{ numbers }")` runs the query without any HTTP server; each element of the resolved list `result.data["numbers"]` is printed on its own line.

## Run

    python3 main.py
