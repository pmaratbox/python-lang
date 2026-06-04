from collections import OrderedDict

counts = OrderedDict()
for ch in "aab":
    counts[ch] = counts.get(ch, 0) + 1

print(" ".join("{}:{}".format(k, v) for k, v in counts.items()))
