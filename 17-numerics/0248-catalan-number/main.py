cats = []
c = 1
for n in range(5):
    cats.append(c)
    c = c * 2 * (2 * n + 1) // (n + 2)
print(" ".join(str(x) for x in cats))
