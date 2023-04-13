import numpy as np

a = np.array([[1.5, 2.3, -3.7],
              [2.8, 3.4, 5.8],
              [1.2, 7.3, -2.3]])

arow = np.array([[1.5, -0.7, -0.7],
                 [1.2, 4.9, 0.1],
                 [2.8, -2.2, 11.4]])

acol = np.array([[1.5, -0.7, -0.7],
                 [2.8, 11.4, -2.2],
                 [1.2, 0.1, 4.9]])

b = np.array([4.5, -3.2, 5.6])
brow = np.array([4.5, 5.6, -3.2])
bcol = np.array([4.5, -3.2, 5.6])

x = np.linalg.solve(a, b)
r = np.allclose(np.dot(a, x), b)
# [ 0.10541962  0.47263511 -0.87967833]

xrow = np.linalg.solve(arow, brow)
rrow = np.allclose(np.dot(arow, xrow), brow)

xcol = np.linalg.solve(acol, bcol)
rcol = np.allclose(np.dot(acol, xcol), bcol)

print("org", x, r)
print("row", xrow, rrow)
print("col", xcol, rcol)

print("org", np.linalg.det(a))
print("row", np.linalg.det(arow))
print("col", np.linalg.det(acol))
