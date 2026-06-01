# 0042 — Environment Variables

Read the environment variable `LESSON_ENV_VAR`, falling back to `default` when it is unset, and print `value: default`. `os.environ` is a dict-like view of the environment; `.get(key, default)` returns the value or the fallback when the variable is absent. `os.getenv` is a thin alias.

## Run

    python3 main.py
