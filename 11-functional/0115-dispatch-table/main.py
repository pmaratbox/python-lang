import operator

table = {"add": operator.add, "mul": operator.mul}

print(table["add"](3, 4), table["mul"](3, 4))
