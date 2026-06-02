# 0023 — Modules & Imports

Define `square(n)` in a separate `mathutil` module and import it from the main program, printing `square(8) = 64` across the module boundary. Each `.py` file is a module; `from mathutil import square` runs `mathutil.py` once and binds the name `square`. Imports resolve along `sys.path`, which includes the script's directory, so a sibling file is found automatically.

## Run

    python3 main.py
