class CelsiusSource:
    def __init__(self, celsius):
        self.celsius = celsius


class FahrenheitAdapter:
    def __init__(self, source):
        self._source = source

    def fahrenheit(self):
        return self._source.celsius * 9 // 5 + 32


def main():
    adapter = FahrenheitAdapter(CelsiusSource(100))
    print(adapter.fahrenheit())


if __name__ == "__main__":
    main()
