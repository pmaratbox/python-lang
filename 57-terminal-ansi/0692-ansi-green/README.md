# 0692 — Green text

Uses the `colorama` ANSI library: `Fore.GREEN` (foreground green, ANSI 32) wraps the word `green`, closed by `Fore.RESET` (the foreground reset `\x1b[39m`). The `Fore.*` constants are raw escape strings, so printing them emits ANSI directly without a TTY — no `colorama.init()` needed.

## Run

    python3 main.py
