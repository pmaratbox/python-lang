# 0415 — SwitchMap

Implement switchMap: when a new outer value arrives, cancel the previous inner subscription before starting the new one. We keep the live inner's scheduler tokens in a one-slot list closure and cancel them on each new outer emission.

## Run

    python3 main.py
