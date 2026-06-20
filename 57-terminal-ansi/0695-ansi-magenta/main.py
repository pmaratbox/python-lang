# colorama provides raw ANSI escape constants. Do NOT call colorama.init()
# (it wraps stdout and strips codes when there's no TTY). The Fore.* values are
# themselves raw escape strings; Fore.RESET is \x1b[39m (foreground reset).
from colorama import Fore

print(Fore.MAGENTA + "magenta" + Fore.RESET)  # \x1b[35mmagenta\x1b[39m
