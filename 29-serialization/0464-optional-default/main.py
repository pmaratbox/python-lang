from pydantic import BaseModel


class Person(BaseModel):
    age: int = 0
    name: str


p = Person.model_validate_json('{"name":"alice"}')
print(p.name, p.age)
