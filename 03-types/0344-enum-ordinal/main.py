from enum import Enum


class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3


members = list(Direction)
ordinal_s = members.index(Direction.S)
name_at_3 = members[3].name
print(ordinal_s, name_at_3)
