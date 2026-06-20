# 0695 — Magenta text

Color the word `magenta` with the foreground MAGENTA color (ANSI 35) using
Python's real ANSI library [colorama](https://pypi.org/project/colorama/). The
`Fore.MAGENTA` constant is a raw escape string and `Fore.RESET` is the
foreground reset `\x1b[39m`; printing them directly (without `colorama.init()`,
which would strip codes on a non-TTY) emits the raw sequence
`ESC[35mmagentaESC[39m`.

## Run

    python3 main.py
