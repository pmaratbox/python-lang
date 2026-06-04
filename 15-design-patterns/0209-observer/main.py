class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, value):
        print("{}: {}".format(self.name, value))


class Subject:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def notify(self, value):
        for observer in self._observers:
            observer.update(value)


def main():
    subject = Subject()
    subject.register(Observer("obs1"))
    subject.register(Observer("obs2"))
    subject.notify(5)


if __name__ == "__main__":
    main()
