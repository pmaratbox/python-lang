import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"


schema = strawberry.Schema(query=Query)

result = schema.execute_sync("{ hello }")

print(result.data["hello"])
