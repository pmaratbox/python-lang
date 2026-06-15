# 0545 — Basic transition

Model a turnstile as a finite state machine with the `transitions` library: a `Machine` holds the `locked`/`unlocked` states, starts in `locked`, and declares two transitions (`coin` unlocks, `push` re-locks). Firing the `coin` trigger fires the matching transition so the machine advances to `unlocked`; reading `model.state` returns the resulting state name, which we lowercase before printing.

## Run

    python3 main.py
