from pydantic import BaseModel


class Address(BaseModel):
    city: str
    zip: int


class Person(BaseModel):
    address: Address
    name: str


person = Person(name="alice", address=Address(city="oslo", zip=1000))
print(person.model_dump_json())
