from dataclasses import dataclass, replace

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
p2 = replace(p1, x=9)
print(f"original: ({p1.x}, {p1.y})")
print(f"updated: ({p2.x}, {p2.y})")
