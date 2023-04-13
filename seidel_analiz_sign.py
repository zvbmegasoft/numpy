# https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve
# https://numpy.org/doc/stable/reference/routines.linalg.html

import numpy as np

aorg = np.array([[ 1.5,  2.3,  -3.7],
                 [ 2.8,  3.4,   5.8],
                 [ 1.2,  7.3,  -2.3]])

arow = np.array([[-1.5,  0.7,   0.7],
                 [-1.2, -4.9,  -0.1],
                 [-2.8,  2.2, -11.4]])

acol = np.array([[-1.5,   0.7,  0.7],
                 [-2.8, -11.4,  2.2],
                 [-1.2,  -0.1, -4.9]])

borg = np.array([ 4.5, -3.2,  5.6])
brow = np.array([-4.5, -5.6,  3.2])
bcol = np.array([-4.5,  3.2, -5.6])

xorg = np.linalg.solve(aorg, borg)
rorg = np.allclose(np.dot(aorg, xorg), borg)

xrow = np.linalg.solve(arow, brow)
rrow = np.allclose(np.dot(arow, xrow), brow)

xcol = np.linalg.solve(acol, bcol)
rcol = np.allclose(np.dot(acol, xcol), bcol)

print("ORG", "[ 0.10541962  0.47263511 -0.87967833]")
print("org", xorg, rorg)
print("row", xrow, rrow)
print("col", xcol, rcol)

print("org", np.linalg.det(aorg))
print("row", np.linalg.det(arow))
print("col", np.linalg.det(acol))
