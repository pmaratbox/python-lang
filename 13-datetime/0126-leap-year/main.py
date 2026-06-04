def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(" ".join("yes" if is_leap(y) else "no" for y in (2000, 1900, 2024)))
