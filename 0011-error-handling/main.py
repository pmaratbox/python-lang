def divide(a: int, b: int) -> int:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a // b


print(f"10 / 2 = {divide(10, 2)}")

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"error: {e}")
