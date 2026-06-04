from dataclasses import dataclass


@dataclass
class Point:
    x: int = 0
    y: int = 0


a = Point()
b = Point(x=5)
print(a.x, a.y)
print(b.x, b.y)
