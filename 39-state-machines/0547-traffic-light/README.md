# 0547 — Traffic light

A finite state machine built with the `transitions` library. We declare the states `red`, `green`, `yellow` and the cyclic `next` transition between them, then fire the `next` event twice from the initial `red` state to advance through `green` to `yellow`. The final state is read back from the machine and lowercased.

## Run

    python3 main.py
