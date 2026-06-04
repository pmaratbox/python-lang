n = 258
encoded = n.to_bytes(2, "big")
high, low = encoded[0], encoded[1]
decoded = int.from_bytes(encoded, "big")
print("{} {} {}".format(high, low, decoded))
