import strawberry


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="alice", age=30)


schema = strawberry.Schema(query=Query)

result = schema.execute_sync("{ user { name age } }")

user = result.data["user"]
print(user["name"])
print(user["age"])
