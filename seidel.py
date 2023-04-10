import numpy as np
a = np.array([[1.5, 2.3, -3.7],
              [2.8, 3.4, 5.8],
              [1.2, 7.3, -2.3]])
b = np.array([4.5, -3.2, 5.6])
x = np.linalg.solve(a, b)
r = np.allclose(np.dot(a, x), b)
print(x, r)
# [ 0.10541962  0.47263511 -0.87967833]
