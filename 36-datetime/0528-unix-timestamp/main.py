import pendulum

# Parse a FIXED UTC instant with pendulum (never the current time),
# then ask the library for its Unix timestamp (epoch SECONDS).
dt = pendulum.parse("2026-06-15T00:00:00Z")
print(dt.int_timestamp)
