# 0551 — Reset

Model a process as a finite state machine with the `transitions` library: a `Machine` holds the `idle`/`running` states, starts in `idle`, and declares a `start` transition (`idle` to `running`) plus a `reset` transition (`running` back to `idle`). A reset event returns the machine to its initial state. After firing `start` then `reset`, reading `model.state` returns the resulting state name, which we lowercase before printing.

## Run

    python3 main.py
