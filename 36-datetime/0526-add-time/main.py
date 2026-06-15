import pendulum

start = pendulum.parse("2026-06-15T10:00")
result = start.add(minutes=90)
print(result.format("HH:mm"))
