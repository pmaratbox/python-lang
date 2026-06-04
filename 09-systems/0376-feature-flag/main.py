def describe(flag):
    return "enabled" if flag else "disabled"


print("{} {}".format(describe(True), describe(False)))
