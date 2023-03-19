import numpy as np
a = np.array([[1, 2], [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)
print(x)
r = np.allclose(np.dot(a, x), b)
print(r)
