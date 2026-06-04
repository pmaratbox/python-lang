import bisect

a = [1, 3, 5, 5, 7]
print(bisect.bisect_left(a, 5), bisect.bisect_right(a, 5))
