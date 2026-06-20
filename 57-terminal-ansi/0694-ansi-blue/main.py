# colorama's Fore.* constants are raw ANSI escape strings; Fore.BLUE -> \x1b[34m and
# Fore.RESET -> \x1b[39m (foreground reset). Do NOT call colorama.init(): on a non-TTY it
# would wrap stdout and strip the codes. Printing the constants directly emits raw ANSI.
from colorama import Fore

print(Fore.BLUE + "blue" + Fore.RESET)  # \x1b[34mblue\x1b[39m
