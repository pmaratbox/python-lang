nums = [1, 2, 2, 3, 1]
unique = list(dict.fromkeys(nums))
print(" ".join(str(x) for x in unique))
