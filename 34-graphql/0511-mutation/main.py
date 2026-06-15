import strawberry


@strawberry.type
class User:
    name: str


@strawberry.type
class Query:
    @strawberry.field
    def ok(self) -> bool:
        return True


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, name: str) -> User:
        return User(name=name)


schema = strawberry.Schema(query=Query, mutation=Mutation)
result = schema.execute_sync('mutation { addUser(name: "bob") { name } }')
print(result.data["addUser"]["name"])
