import numpy as np

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
c = a + b
print(" ".join(str(int(x)) for x in c))
