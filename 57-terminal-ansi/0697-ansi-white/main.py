# Color "white" with the foreground WHITE color using colorama.
# The Fore.* constants are raw ANSI escape strings, so we do NOT call colorama.init()
# (that wraps stdout and strips codes on a non-TTY). Fore.WHITE is \x1b[37m and
# Fore.RESET is \x1b[39m (foreground reset). Printing them directly emits the raw bytes.
from colorama import Fore

print(Fore.WHITE + "white" + Fore.RESET)  # \x1b[37mwhite\x1b[39m
