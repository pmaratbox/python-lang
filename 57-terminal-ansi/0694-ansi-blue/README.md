# 0694 — Blue text

Uses the [colorama](https://pypi.org/project/colorama/) library's `Fore.BLUE` constant (foreground BLUE, ANSI 34) to color the word `blue`, then resets with `Fore.RESET` (the foreground reset `\x1b[39m`). The `Fore.*` constants are raw escape strings, so we print them directly without calling `colorama.init()` — that emits the raw ANSI sequence even without a TTY: `ESC[34mblueESC[39m`.

## Run

    python3 main.py
