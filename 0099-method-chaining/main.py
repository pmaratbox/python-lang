class Calc:
    def __init__(self, value):
        self.value = value

    def add(self, n):
        self.value += n
        return self

    def multiply(self, n):
        self.value *= n
        return self

    def result(self):
        return self.value


print(Calc(5).add(3).multiply(2).result())
