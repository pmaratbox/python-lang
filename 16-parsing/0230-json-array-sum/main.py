def sum_array(text):
    inner = text.strip()[1:-1].strip()
    if not inner:
        return 0
    return sum(int(part) for part in inner.split(","))


print(sum_array("[1,2,3]"))
