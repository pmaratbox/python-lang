from dataclasses import dataclass


@dataclass
class Address:
    city: str


@dataclass
class Person:
    name: str
    address: Address


person = Person("Ada", Address("London"))
print(person.address.city)
