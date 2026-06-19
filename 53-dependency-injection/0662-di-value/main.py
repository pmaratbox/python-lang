from dependency_injector import containers, providers


class ValueService:
    """A service that receives an injected constant and returns it."""

    def __init__(self, value: str):
        self.value = value

    def get(self) -> str:
        return self.value


class Container(containers.DeclarativeContainer):
    # Register the constant value `v1` as an Object provider.
    config = providers.Object("v1")
    # The service receives the value via constructor injection.
    service = providers.Factory(ValueService, value=config)


def main() -> None:
    container = Container()
    service = container.service()  # resolve the graph through the container
    print(service.get())


if __name__ == "__main__":
    main()
