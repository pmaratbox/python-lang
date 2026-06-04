from typing import NewType

Meters = NewType("Meters", int)

distance = Meters(5)
print(f"distance: {distance}")
