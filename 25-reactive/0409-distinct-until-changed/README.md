# 0409 — Distinct Until Changed

Implement distinctUntilChanged, dropping consecutive duplicate values from 1,1,2,2,2,3,1. A small closure-captured state dict tracks the last emitted value and forwards only when the new value differs.

## Run

    python3 main.py
