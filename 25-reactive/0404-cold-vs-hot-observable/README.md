# 0404 — Cold vs Hot Observable

Contrast a cold observable (re-runs its producer per subscriber) with a hot one (shares a single execution, so late subscribers miss earlier values). The cold observable stores a producer callable invoked fresh on each `subscribe`, while the hot one keeps a list of observers and multicasts each `emit` to whoever is currently subscribed.

## Run

    python3 main.py
