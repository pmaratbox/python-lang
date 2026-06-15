from pydantic import BaseModel


class Person(BaseModel):
    age: int
    name: str


p = Person.model_validate_json('{"age":30,"name":"alice"}')
print(p.name, p.age)
