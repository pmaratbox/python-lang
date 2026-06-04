class Memento:
    def __init__(self, state):
        self.state = state


class Originator:
    def __init__(self, state):
        self.state = state

    def save(self):
        return Memento(self.state)

    def restore(self, memento):
        self.state = memento.state


def main():
    originator = Originator(1)
    memento = originator.save()
    originator.state = 2
    print(originator.state, end=" ")
    originator.restore(memento)
    print(originator.state)


if __name__ == "__main__":
    main()
