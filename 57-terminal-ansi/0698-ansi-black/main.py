# Color "black" with the foreground BLACK color using colorama.
# The Fore.* constants are raw ANSI escape strings, so we do NOT call colorama.init()
# (that wraps stdout and strips codes on a non-TTY). Fore.BLACK is \x1b[30m and
# Fore.RESET is \x1b[39m (foreground reset). Printing them directly emits the raw bytes.
from colorama import Fore

print(Fore.BLACK + "black" + Fore.RESET)  # \x1b[30mblack\x1b[39m
