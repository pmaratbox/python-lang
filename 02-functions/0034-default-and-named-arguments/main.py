def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"

print(greet("Ada"))
print(greet("Ada", greeting="Hi"))
