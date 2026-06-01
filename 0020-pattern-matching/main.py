def word(n: int) -> str:
    if n == 1:
        return "one"
    if n == 2:
        return "two"
    return "many"

for n in [1, 2, 5]:
    print(f"{n}: {word(n)}")
