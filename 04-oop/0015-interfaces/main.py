from abc import ABC, abstractmethod
from dataclasses import dataclass


class Shape(ABC):
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def area(self) -> int: ...


@dataclass
class Rectangle(Shape):
    width: int
    height: int

    def name(self) -> str:
        return "rectangle"

    def area(self) -> int:
        return self.width * self.height


@dataclass
class Square(Shape):
    side: int

    def name(self) -> str:
        return "square"

    def area(self) -> int:
        return self.side * self.side


shapes: list[Shape] = [Rectangle(3, 4), Square(5)]
for s in shapes:
    print(f"{s.name()} area: {s.area()}")
