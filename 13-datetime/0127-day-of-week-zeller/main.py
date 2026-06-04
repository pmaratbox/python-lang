def zeller_weekday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    # h: 0=Saturday, 1=Sunday, 2=Monday, ...
    names = ["Saturday", "Sunday", "Monday", "Tuesday",
             "Wednesday", "Thursday", "Friday"]
    return names[h]


print(zeller_weekday(2000, 1, 1))
