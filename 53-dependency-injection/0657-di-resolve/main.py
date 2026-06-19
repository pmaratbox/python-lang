from dependency_injector import containers, providers


class Greeter:
    def greet(self):
        return "hello"


class Container(containers.DeclarativeContainer):
    greeter = providers.Factory(Greeter)


container = Container()
greeter = container.greeter()  # resolved through the container
print(greeter.greet())
