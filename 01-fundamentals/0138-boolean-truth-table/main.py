def s(b):
    return "true" if b else "false"


for a, b in ((True, True), (True, False), (False, True), (False, False)):
    print(s(a), s(b), s(a and b), s(a or b), s(a != b))
