from pydantic import BaseModel


class Person(BaseModel):
    age: int
    name: str


person = Person(age=30, name="alice")
data = person.model_dump_json()
restored = Person.model_validate_json(data)
print(restored.name)
