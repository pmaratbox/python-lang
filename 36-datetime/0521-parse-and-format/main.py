import pendulum

# Parse a FIXED ISO date with pendulum (never the current time),
# then format it back to ISO (YYYY-MM-DD) using the library.
dt = pendulum.parse("2026-06-15")
print(dt.format("YYYY-MM-DD"))
