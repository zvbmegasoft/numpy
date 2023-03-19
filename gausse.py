import numpy as np
a = np.array([[13.21, 6.15, 7.11, 0.82],
              [-10.15, -3.16, 2.22, -0.18],
              [-7.10, 2.32, -0.91, 0.98],
              [3.45, 16.21, 96.21, 103.22]])
b = np.array([1.12, 2.45, 126.17, 0.15])
x = np.linalg.solve(a, b)
r = np.allclose(np.dot(a, x), b)
print(x, r)
