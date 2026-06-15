# 0550 — Transition count

Using the `transitions` library, this turnstile FSM registers an `after_state_change` callback that runs on every state change. Each of the three valid events (`coin`, `push`, `coin`) advances the machine and fires the callback, which increments a counter held on the model. The printed total comes entirely from these per-transition actions, demonstrating how a finite state machine can attach side effects to its transitions.

## Run

    python3 main.py
