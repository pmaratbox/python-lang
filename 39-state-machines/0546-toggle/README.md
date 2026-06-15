# 0546 — Toggle

Use the `transitions` finite-state-machine library: a single `toggle` trigger is defined twice so it flips between the two states (`off --toggle--> on` and `on --toggle--> off`). Starting from `off`, firing `toggle` three times walks `off -> on -> off -> on`, and the machine's resulting `state` is printed lowercased.

## Run

    python3 main.py
