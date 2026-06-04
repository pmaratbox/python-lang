# 0323 — Maybe Monad

Chain Maybe operations: Some(2) then +3 then *2 gives 10, and a None chain yields the fallback, printing `10 none`. A small `Maybe` class with `bind` short-circuits on the absent case.

## Run

    python3 main.py
