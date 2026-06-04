def opt_map(opt, f):
    return None if opt is None else f(opt)


def unwrap_or(opt, default):
    return default if opt is None else opt


present = opt_map(10, lambda x: x + 2)
absent = opt_map(None, lambda x: x + 2)
print(unwrap_or(present, "none"), unwrap_or(absent, "none"))
