import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def greet(self, name: str) -> str:
        return "hello " + name


schema = strawberry.Schema(query=Query)
result = schema.execute_sync('{ greet(name: "alice") }')
print(result.data["greet"])
