from colorama import Fore

# Fore.* constants are raw ANSI escape strings; Fore.CYAN is \x1b[36m and
# Fore.RESET is \x1b[39m (foreground reset). Do NOT call colorama.init():
# that wraps stdout and strips codes when there is no TTY. Printing the
# constants directly emits the raw ANSI bytes.
print(Fore.CYAN + "cyan" + Fore.RESET)
