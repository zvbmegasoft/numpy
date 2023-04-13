import numpy as np
a = np.array([[1.5, -0.7, -0.7],
              [1.2, 4.9, 0.1],
              [2.8, -2.2, 11.4]])
b = np.array([4.5, 5.6, -3.2])
x = np.linalg.solve(a, b)
r = np.allclose(np.dot(a, x), b)
print(x, r)
# [ 0.10541962  0.47263511 -0.87967833]
