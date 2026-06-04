def reverse_integer(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result


if __name__ == "__main__":
    print(reverse_integer(1234))
