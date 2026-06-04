class Handler:
    def __init__(self, level):
        self._level = level
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, level):
        if level == self._level:
            print("handled by {}".format(self._level))
        elif self._next is not None:
            self._next.handle(level)


def main():
    h1 = Handler(1)
    h2 = Handler(2)
    h3 = Handler(3)
    h1.set_next(h2).set_next(h3)
    h1.handle(2)


if __name__ == "__main__":
    main()
