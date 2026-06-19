from dependency_injector import containers, providers


class Widget:
    def __init__(self, label):
        self.label = label

    def value(self):
        return self.label


def build_widget():
    # factory function that constructs the service
    return Widget("built")


class Container(containers.DeclarativeContainer):
    widget = providers.Factory(build_widget)


container = Container()
widget = container.widget()  # built by the factory provider through the container
print(widget.value())
