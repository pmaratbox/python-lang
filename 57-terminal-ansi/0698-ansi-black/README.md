# 0698 — Black text

Uses the [colorama](https://pypi.org/project/colorama/) ANSI library and its `Fore.BLACK` constant to color the word `black` with the foreground BLACK color (ANSI 30), forced on without a TTY since the `Fore.*` constants are raw escape strings. It closes with `Fore.RESET` (the foreground reset `\x1b[39m`), printing the raw sequence `ESC[30mblackESC[39m`.

## Run

    python3 main.py
