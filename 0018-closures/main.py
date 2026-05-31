def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


next_count = make_counter()
print(f"count: {next_count()}")
print(f"count: {next_count()}")
