class Mediator:
    def __init__(self):
        self.colleague_b = None

    def route(self, message):
        self.colleague_b.receive(message)


class ColleagueA:
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, message):
        self._mediator.route(message)


class ColleagueB:
    def receive(self, message):
        print("B got: {}".format(message))


def main():
    mediator = Mediator()
    a = ColleagueA(mediator)
    b = ColleagueB()
    mediator.colleague_b = b
    a.send("hi")


if __name__ == "__main__":
    main()
