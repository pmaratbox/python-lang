def inc(box: list[int]) -> None:
    box[0] += 1

box = [1]
print(f"before: {box[0]}")
inc(box)
print(f"after: {box[0]}")
