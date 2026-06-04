class Sub1:
    def init(self):
        pass


class Sub2:
    def init(self):
        pass


class Sub3:
    def init(self):
        pass


class Facade:
    def __init__(self):
        self._sub1 = Sub1()
        self._sub2 = Sub2()
        self._sub3 = Sub3()

    def start(self):
        self._sub1.init()
        self._sub2.init()
        self._sub3.init()
        return "ready"


def main():
    print(Facade().start())


if __name__ == "__main__":
    main()
