class RealSubject:
    def request(self):
        return "loaded"


class Proxy:
    def __init__(self):
        self._real = None

    def request(self):
        if self._real is None:
            self._real = RealSubject()
        return self._real.request()


def main():
    print(Proxy().request())


if __name__ == "__main__":
    main()
