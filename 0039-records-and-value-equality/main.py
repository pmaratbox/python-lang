from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = Point(1, 2)
print(f"point: ({p1.x}, {p1.y})")
print("equal:", "yes" if p1 == p2 else "no")
