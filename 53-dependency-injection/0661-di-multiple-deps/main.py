from dependency_injector import containers, providers


class A:
    def x(self):
        return "a"


class B:
    def y(self):
        return "b"


class Service:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def run(self):
        return self.a.x() + self.b.y()


class Container(containers.DeclarativeContainer):
    a = providers.Singleton(A)
    b = providers.Singleton(B)
    service = providers.Factory(Service, a=a, b=b)


container = Container()
print(container.service().run())
