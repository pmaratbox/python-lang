LEVELS = {"INFO": 1, "WARN": 2, "ERROR": 3}

threshold = LEVELS["WARN"]

messages = [("INFO", "i"), ("WARN", "w"), ("ERROR", "e")]

for level, msg in messages:
    if LEVELS[level] >= threshold:
        print("{}: {}".format(level, msg))
