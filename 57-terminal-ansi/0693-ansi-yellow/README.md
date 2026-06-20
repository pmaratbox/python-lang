# 0693 — Yellow text

Python's `colorama` library colors the word `yellow` with the foreground YELLOW color via `Fore.YELLOW`, whose constant is a raw ANSI escape string (`\x1b[33m`); concatenating it before the word and closing with `Fore.RESET` (the foreground reset `\x1b[39m`) emits the raw sequence directly to stdout without any TTY, since `colorama.init()` is not called.

## Run

    python3 main.py
