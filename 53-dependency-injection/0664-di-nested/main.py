from dependency_injector import containers, providers


class A:
    def v(self):
        return "a"


class B:
    def __init__(self, a):
        self.a = a

    def v(self):
        return self.a.v() + "b"


class C:
    def __init__(self, b):
        self.b = b

    def v(self):
        return self.b.v() + "c"


class Container(containers.DeclarativeContainer):
    a = providers.Singleton(A)
    b = providers.Singleton(B, a=a)
    c = providers.Singleton(C, b=b)


container = Container()

# Resolve C through the container; it wires the whole A -> B -> C graph.
c = container.c()
print(c.v())
