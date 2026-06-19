from abc import ABC, abstractmethod

from dependency_injector import containers, providers


class Animal(ABC):
    @abstractmethod
    def sound(self) -> str: ...


class Dog(Animal):
    def sound(self) -> str:
        return "woof"


class Container(containers.DeclarativeContainer):
    # Bind the Animal interface to the Dog implementation.
    animal = providers.Factory(Dog)


container = Container()
animal = container.animal()  # resolved by interface through the container
print(animal.sound())
