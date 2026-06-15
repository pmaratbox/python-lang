import pendulum

# Parse a FIXED ISO date with pendulum (never the current time),
# then ask the library for its ISO weekday number (Mon=1 .. Sun=7).
dt = pendulum.parse("2026-06-15")
print(dt.isoweekday())
