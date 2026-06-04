class Greeter:
    def greet(self):
        return "hi"


class LoudGreeter(Greeter):
    def greet(self):
        return "hey"


def main():
    default = Greeter()
    override = LoudGreeter()
    print(default.greet(), override.greet())


if __name__ == "__main__":
    main()
