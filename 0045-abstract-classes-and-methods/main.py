from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        ...

    def describe(self) -> str:
        return f"area: {self.area()}"

class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side = side

    def area(self) -> int:
        return self.side * self.side

print(Square(3).describe())
