import pendulum

# Parse a FIXED date (never the current time) at a fixed UTC offset.
dt = pendulum.parse("2026-06-15T00:00:00+00:00")

# The library computes each calendar component from the instant.
print(dt.year)
print(dt.month)
print(dt.day)
