# 0511 — Mutation

Using strawberry-graphql, define a `Mutation` type with `addUser(name: String!): User` and execute the mutation in-process with `schema.execute_sync`. The resolver constructs and returns a `User`, and the resolved name is read from the execution result's `data` (`data.addUser.name`).

## Run

    python3 main.py
