from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p = Person("Ada", 36)
print(f"name: {p.name}")
print(f"age: {p.age}")
