import strawberry
from typing import List


@strawberry.type
class Query:
    @strawberry.field
    def numbers(self) -> List[int]:
        return [1, 2, 3]


schema = strawberry.Schema(query=Query)
result = schema.execute_sync("{ numbers }")
for n in result.data["numbers"]:
    print(n)
