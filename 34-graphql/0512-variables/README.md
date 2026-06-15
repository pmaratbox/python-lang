# 0512 — Query variables

Using strawberry-graphql, define `Query.item(id: Int!): Item { id: Int }` and execute the query `query($id: Int!) { item(id: $id) { id } }` in-process with `schema.execute_sync`, passing `id` through the execution's `variable_values` map (a GraphQL query variable) rather than interpolating it into the query string. The resolver returns the `Item`, and `data.item.id` is read from the execution result.

## Run

    python3 main.py
