data = "alice,30\nbob,25"

pairs = []
for line in data.splitlines():
    name, value = line.split(",")
    pairs.append(name + "=" + value)

print(" ".join(pairs))
