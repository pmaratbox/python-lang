from dependency_injector import containers, providers


class Repo:
    def data(self):
        return "data"


class Service:
    def __init__(self, repo):
        self.repo = repo

    def run(self):
        return self.repo.data()


class Container(containers.DeclarativeContainer):
    repo = providers.Singleton(Repo)
    service = providers.Factory(Service, repo=repo)


container = Container()
service = container.service()  # resolves the Service -> Repo graph
print(service.run())
