import copy


class Prototype:
    def __init__(self, value):
        self.value = value


def main():
    original = Prototype(1)
    clone = copy.deepcopy(original)
    clone.value = 2
    print(original.value, clone.value)


if __name__ == "__main__":
    main()
