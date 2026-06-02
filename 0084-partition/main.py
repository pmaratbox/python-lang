nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print("evens:", " ".join(str(x) for x in evens))
print("odds:", " ".join(str(x) for x in odds))
