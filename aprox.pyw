# importing the required packages and libraries
from scipy.optimize import curve_fit
from numpy import array, exp
import matplotlib.pyplot as plt

# defining the variables
values_y = array([11, 10, 12, 14, 15, 15, 14, 13, 14, 11, 10, 11, 7, 9, 8, 6, 5])
values_x = array(range(len(values_y)))


# defining objective functions
def mapping1(values_x, a, b, c):
    return a * values_x**2 + b * values_x + c


def mapping2(values_x, a, b, c):
    return a * values_x**3 + b * values_x + c


def mapping3(values_x, a, b, c):
    return a * values_x**3 + b * values_x**2 + c


def mapping4(values_x, a, b, c):
    return a * exp(b * values_x) + c


# using the curve_fit() function
args, covar = curve_fit(mapping1, values_x, values_y)
print("Arguments: ", args)
print("Co-Variance: ", covar)

args, _ = curve_fit(mapping1, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit1 = a * values_x**2 + b * values_x + c

args, _ = curve_fit(mapping2, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit2 = a * values_x**3 + b * values_x + c

args, _ = curve_fit(mapping3, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit3 = a * values_x**3 + b * values_x**2 + c

args, _ = curve_fit(mapping4, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit4 = a * exp(values_x * b) + c

# plotting the graph
plt.plot(values_x, values_y, "bo", label="y - original")
plt.plot(values_x, y_fit1, label="y = a * x^2 + b * x + c")
plt.plot(values_x, y_fit2, label="y = a * x^3 + b * x + c")
plt.plot(values_x, y_fit3, label="y = a * x^3 + b * x^2 * c")
plt.plot(values_x, y_fit4, label="y = a * exp(b * x) + c")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best", fancybox=True, shadow=True)
plt.grid(True)
plt.show()

# https://pythonpip.ru/examples/podgonka-krivoy-v-python-s-pomoschyu-biblioteki-scipy
