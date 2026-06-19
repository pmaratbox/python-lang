from dependency_injector import containers, providers


class Repo:
    def data(self):
        return "data"


class Container(containers.DeclarativeContainer):
    repo = providers.Singleton(Repo)  # Singleton: same instance every resolve


container = Container()
first = container.repo()  # resolved through the container
second = container.repo()  # resolved again
print(str(first is second).lower())  # same instance -> true
