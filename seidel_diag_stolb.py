import numpy as np
a = np.array([[1.5, -0.7, -0.7],
              [2.8, 11.4, -2.2],
              [1.2, 0.1, 4.9]])
b = np.array([4.5, -3.2, 5.6])
x = np.linalg.solve(a, b)
r = np.allclose(np.dot(a, x), b)
print(x, r)
# [ 0.10541962  0.47263511 -0.87967833]
# [ 0.10541962 -0.87967833  0.47263511] OK
