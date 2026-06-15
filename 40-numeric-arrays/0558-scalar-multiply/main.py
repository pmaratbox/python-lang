import numpy as np

a = np.array([[1, 2], [3, 4]])
scalar = 3
c = scalar * a
for row in c:
    print(" ".join(str(int(x)) for x in row))
