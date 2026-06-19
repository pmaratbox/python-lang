import toolz

g = toolz.groupby(lambda x: "even" if x % 2 == 0 else "odd", range(1, 7))
print(";".join(f"{k}:{','.join(map(str, g[k]))}" for k in sorted(g)))
