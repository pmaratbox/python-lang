from pydantic import BaseModel, TypeAdapter


class Person(BaseModel):
    age: int
    name: str


people = [Person(age=30, name="alice"), Person(age=25, name="bob")]
adapter = TypeAdapter(list[Person])
print(adapter.dump_json(people).decode())
