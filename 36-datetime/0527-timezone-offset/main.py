import pendulum

# Parse a FIXED UTC instant with pendulum (never the current time),
# then convert it to a FIXED +05:00 offset using a fixed-offset zone
# (FixedTimezone takes seconds: 5 hours = 5 * 3600), NOT a named tz / OS tzdata.
utc = pendulum.parse("2026-06-15T12:00:00Z")
local = utc.in_timezone(pendulum.FixedTimezone(5 * 3600))
print(local.hour)
