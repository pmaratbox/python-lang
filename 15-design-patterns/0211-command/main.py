class Counter:
    def __init__(self):
        self.value = 0


class AddCommand:
    def __init__(self, counter, amount):
        self._counter = counter
        self._amount = amount

    def execute(self):
        self._counter.value += self._amount

    def undo(self):
        self._counter.value -= self._amount


def main():
    counter = Counter()
    command = AddCommand(counter, 5)
    command.execute()
    print(counter.value, end=" ")
    command.undo()
    print(counter.value)


if __name__ == "__main__":
    main()
