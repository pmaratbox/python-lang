n = 2.0
x = n
while True:
    nxt = x - (x * x - n) / (2 * x)
    if abs(nxt - x) < 1e-12:
        x = nxt
        break
    x = nxt
print("{:.4f}".format(x))
