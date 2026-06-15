import strawberry


@strawberry.type
class Address:
    city: str


@strawberry.type
class User:
    address: Address


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(address=Address(city="oslo"))


schema = strawberry.Schema(query=Query)
result = schema.execute_sync("{ user { address { city } } }")
print(result.data["user"]["address"]["city"])
