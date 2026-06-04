nums = [2, 4, 6]
all_even = all(n % 2 == 0 for n in nums)
any_odd = any(n % 2 == 1 for n in nums)
print(("yes" if all_even else "no") + " " + ("yes" if any_odd else "no"))
