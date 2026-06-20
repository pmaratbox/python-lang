from colorama import Fore

# Do NOT call colorama.init(): that wraps stdout and strips codes off a non-TTY.
# The Fore.* constants are raw escape strings, so printing them emits ANSI directly.
# Fore.RESET is the foreground reset \x1b[39m (not the full reset \x1b[0m).
print(Fore.RED + "red" + Fore.RESET)
