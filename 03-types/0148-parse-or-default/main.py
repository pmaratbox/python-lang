def parse_or_default(text, default):
    try:
        return int(text)
    except ValueError:
        return default


print(f"{parse_or_default('42', 0)} {parse_or_default('x', 0)}")
