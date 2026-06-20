# 0696 — Cyan text

Uses `colorama`'s `Fore.CYAN` constant to color the word `cyan` with the foreground CYAN color (ANSI 36), then resets with `Fore.RESET`. The `Fore.*` values are raw ANSI escape strings, so printing them directly emits the sequence `ESC[36mcyanESC[39m` without needing a TTY (we deliberately skip `colorama.init()`, which would strip codes on non-terminal output).

## Run

    python3 main.py
