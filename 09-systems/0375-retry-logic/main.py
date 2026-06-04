def attempt(n):
    return n >= 3


for n in range(1, 4):
    if attempt(n):
        print("ok after {}".format(n))
        break
