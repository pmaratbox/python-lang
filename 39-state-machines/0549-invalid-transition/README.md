# 0549 — Invalid transition

Using the `transitions` library, this turnstile FSM starts in `locked` and fires `push`, an event that has no transition defined from the `locked` state. The machine raises `MachineError`, which we catch; the state remains unchanged because an invalid event never advances a finite state machine. We then print the state name lowercased.

## Run

    python3 main.py
