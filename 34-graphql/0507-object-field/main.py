import strawberry


@strawberry.type
class User:
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="alice")


schema = strawberry.Schema(query=Query)

result = schema.execute_sync("{ user { name } }")

print(result.data["user"]["name"])
