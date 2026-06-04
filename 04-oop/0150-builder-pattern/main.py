class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def __str__(self):
        return "Pizza({}, {})".format(self.size, ", ".join(self.toppings))


class PizzaBuilder:
    def __init__(self):
        self._size = None
        self._toppings = []

    def set_size(self, size):
        self._size = size
        return self

    def add_topping(self, topping):
        self._toppings.append(topping)
        return self

    def build(self):
        return Pizza(self._size, self._toppings)


pizza = PizzaBuilder().set_size("M").add_topping("cheese").build()
print(pizza)
