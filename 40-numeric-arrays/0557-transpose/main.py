import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
t = a.T
for row in t:
    print(" ".join(str(int(x)) for x in row))
