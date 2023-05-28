# importing the required packages and libraries
from scipy.optimize import curve_fit
from numpy import array
import matplotlib.pyplot as plt

# defining the variables
values_x = array([0.119, 0.473, 0.826, 1.180, 1.533, 1.887, 2.241, 2.594, 2.948])
values_y = array([-0.572, -1.282, -2.155, -3.027, -3.783, -4.418, -5.267, -6.116, -6.742])


# defining objective functions
def mapping_line(values_x, a, b):
    return a * values_x + b


def mapping_square(values_x, a, b, c):
    return a * values_x**2 + b * values_x + c


def mapping_power(values_x, a, b, c):
    return b * values_x**a + c


# using the curve_fit() function
args, _ = curve_fit(mapping_line, values_x, values_y)
a, b = args[0], args[1]
y_fit_line = a * values_x + b
print()
print("line")
print("y = a * x + b")
print("a =", a, "  b =", b)

args, _ = curve_fit(mapping_square, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit_square = a * values_x**2 + b * values_x + c
print()
print("square")
print("y = a * x^2 + b * x + c")
print("a =", a, "  b =", b, "  c =", c)

args, _ = curve_fit(mapping_power, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit_power = b * values_x**a + c
print()
print("power")
print("y = b * x^a + c")
print("a =", a, "  b =", b, "  c =", c)
print()

# plotting the graph
plt.plot(values_x, values_y, "bo", label="y - original")
plt.plot(values_x, y_fit_line, label="y = a * x + b")
plt.plot(values_x, y_fit_square, label="y = a * x^2 + b * x + c")
plt.plot(values_x, y_fit_power, label="y = b * x^a + c")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best", fancybox=True, shadow=True)
plt.grid(True)
plt.show()

# https://pythonpip.ru/examples/podgonka-krivoy-v-python-s-pomoschyu-biblioteki-scipy
