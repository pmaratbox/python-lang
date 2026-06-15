import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a @ b
for row in c:
    print(" ".join(str(int(x)) for x in row))
