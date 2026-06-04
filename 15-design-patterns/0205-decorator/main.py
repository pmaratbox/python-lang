class Coffee:
    def cost(self):
        return 2


class Milk:
    def __init__(self, component):
        self._component = component

    def cost(self):
        return self._component.cost() + 1


class Sugar:
    def __init__(self, component):
        self._component = component

    def cost(self):
        return self._component.cost() + 1


def main():
    drink = Sugar(Milk(Coffee()))
    print(drink.cost())


if __name__ == "__main__":
    main()
