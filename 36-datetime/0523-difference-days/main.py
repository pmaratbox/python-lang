import pendulum

# Two FIXED dates (never the current time). Parse with the real library.
start = pendulum.parse("2026-06-15")
end = pendulum.parse("2026-07-15")

# Let pendulum compute the difference in whole days.
days = end.diff(start).in_days()
print(days)
