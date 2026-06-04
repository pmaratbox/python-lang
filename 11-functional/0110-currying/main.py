def add(a):
    return lambda b: a + b


print(add(2)(3))
