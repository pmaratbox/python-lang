class Rect:
    def __init__(self, w, h):
        self.w = w
        self.h = h


class Square:
    def __init__(self, s):
        self.s = s


def area(shape):
    if isinstance(shape, Rect):
        return shape.w * shape.h
    return shape.s * shape.s


for shape in (Rect(2, 3), Square(4)):
    print(area(shape))
