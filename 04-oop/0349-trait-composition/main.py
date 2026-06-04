class A:
    def a(self):
        return "a"


class B:
    def b(self):
        return "b"


class TraitComposition(A, B):
    pass


def main():
    obj = TraitComposition()
    print(obj.a(), obj.b())


if __name__ == "__main__":
    main()
