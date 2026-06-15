import strawberry


@strawberry.type
class Item:
    id: int


@strawberry.type
class Query:
    @strawberry.field
    def item(self, id: int) -> Item:
        return Item(id=id)


schema = strawberry.Schema(query=Query)
result = schema.execute_sync(
    "query($id: Int!) { item(id: $id) { id } }",
    variable_values={"id": 42},
)
print(result.data["item"]["id"])
