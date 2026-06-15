# 0506 — Field argument

Using strawberry-graphql, define `Query.greet(name: String!)` and execute the query in-process with `schema.execute_sync`, passing the `name` argument as a GraphQL field argument. The resolver returns `'hello ' + name`, and the value is read from the execution result's `data`.

## Run

    python3 main.py
