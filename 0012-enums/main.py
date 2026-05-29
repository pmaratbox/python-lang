from enum import IntEnum


class Color(IntEnum):
    RED = 0
    GREEN = 1
    BLUE = 2


print(f"green: {Color.GREEN.value}")
print(f"blue: {Color.BLUE.value}")
