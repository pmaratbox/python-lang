# 0659 — Singleton lifetime

Register `Repo` as a `providers.Singleton` in a `dependency-injector` `DeclarativeContainer`, then resolve it twice from the container and print whether the two resolutions are the same instance (identity), which prints `true` because a singleton caches one instance.

## Run

    python3 main.py
