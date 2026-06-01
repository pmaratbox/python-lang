class TooLargeError(Exception):
    pass

def check(n: int) -> None:
    if n > 100:
        raise TooLargeError("value too large")

try:
    check(200)
except TooLargeError as e:
    print(f"error: {e}")
