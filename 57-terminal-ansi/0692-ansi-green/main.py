from colorama import Fore

# colorama's Fore.* constants are raw ANSI escape strings (no TTY needed).
# Fore.GREEN is \x1b[32m and Fore.RESET is the foreground reset \x1b[39m.
print(Fore.GREEN + "green" + Fore.RESET)
