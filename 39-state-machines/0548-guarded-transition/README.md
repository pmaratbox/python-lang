# 0548 — Guarded transition

Uses the `transitions` library to build a door FSM (`locked` -> `unlocked` -> `open`). A *guarded transition* is one that is only legal from a specific source state: here the `open` event is defined with `source='unlocked'`, so it can only fire after the door has been unlocked. We fire `unlock` then `open` and print the resulting state lowercased.

## Run

    python3 main.py
