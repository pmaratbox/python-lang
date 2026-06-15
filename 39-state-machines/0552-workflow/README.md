# 0552 — Workflow

Model a multi-step approval workflow as a finite state machine with the `transitions` library: a `Machine` holds the `idle`/`pending`/`approved` states, starts in `idle`, and declares two transitions (`submit` moves to `pending`, `approve` moves to `approved`). Firing the `submit` then `approve` triggers advances the machine through each transition; reading `model.state` returns the resulting state name, which we lowercase before printing.

## Run

    python3 main.py
