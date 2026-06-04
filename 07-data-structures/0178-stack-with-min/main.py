class WithMin:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, value):
        self.stack.append(value)
        if not self.mins or value <= self.mins[-1]:
            self.mins.append(value)
        else:
            self.mins.append(self.mins[-1])

    def pop(self):
        self.mins.pop()
        return self.stack.pop()

    def get_min(self):
        return self.mins[-1]


def main():
    stack = WithMin()
    for value in (3, 1, 2):
        stack.push(value)
    print("min:", stack.get_min())


if __name__ == "__main__":
    main()
