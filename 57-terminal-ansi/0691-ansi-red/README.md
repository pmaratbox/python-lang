# 0691 — Red text

Uses the `colorama` ANSI library to color the word `red` with the foreground RED color (`Fore.RED`, ANSI 31), forced on without a TTY by printing the raw escape constants directly (no `colorama.init()`), and closes with `Fore.RESET` (the foreground reset `\x1b[39m`). The raw sequence is `ESC[31mredESC[39m`.

## Run

    python3 main.py
