# 0658 — Inject a dependency

Register both `Repo` and `Service` in a `dependency-injector` `DeclarativeContainer`. `Service` depends on `Repo`, wired via `providers.Factory(Service, repo=repo)`. Resolving `service` from the container builds the whole graph; calling `run()` delegates to `repo.data()` and returns `data`.

## Run

    python3 main.py
