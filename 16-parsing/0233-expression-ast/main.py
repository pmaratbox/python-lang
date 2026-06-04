class Num:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()


# 1 + 2 * 3
tree = Add(Num(1), Mul(Num(2), Num(3)))
print(tree.eval())
