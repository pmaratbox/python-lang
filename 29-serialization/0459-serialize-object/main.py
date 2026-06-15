from pydantic import BaseModel


class Person(BaseModel):
    age: int
    name: str


person = Person(age=30, name="alice")
print(person.model_dump_json())
