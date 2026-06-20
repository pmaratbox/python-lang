# 0697 — White text

Uses the [colorama](https://pypi.org/project/colorama/) ANSI library and its `Fore.WHITE` constant to color the word `white` with the foreground WHITE color (ANSI 37), forced on without a TTY since the `Fore.*` constants are raw escape strings. It closes with `Fore.RESET` (the foreground reset `\x1b[39m`), printing the raw sequence `ESC[37mwhiteESC[39m`.

## Run

    python3 main.py
