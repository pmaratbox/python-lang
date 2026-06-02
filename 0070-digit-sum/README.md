# 0070 — Digit Sum

Sum the decimal digits of `1234` (repeatedly take the last digit with `% 10` and drop it with `/ 10`) and print the total: `10`. `n % 10` peels off the last digit and `n //= 10` (floor division) drops it, until `n` reaches zero.

## Run

    python3 main.py
