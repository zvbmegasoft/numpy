# importing the required packages and libraries
from scipy.optimize import curve_fit
from numpy import array
import matplotlib.pyplot as plt

# defining the variables
values_x = array([0.079, 0.431, 0.782, 1.134, 1.486, 1.838, 2.189, 2.541, 2.893])
values_y = array([-4.308, -1.778, -0.268, 1.144, 2.248, 3.273, 4.440, 5.396, 6.357])


# defining objective functions
def mapping1(values_x, a, b, c):
    return a * values_x**2 + b * values_x + c


def mapping2(values_x, a, b, c):
    return b * values_x**a + c


# using the curve_fit() function
args, _ = curve_fit(mapping1, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit1 = a * values_x**2 + b * values_x + c
print("mapping1")
print("Arguments: ", args)

args, _ = curve_fit(mapping2, values_x, values_y)
a, b, c = args[0], args[1], args[2]
y_fit2 = b * values_x**a + c
print("mapping2")
print("Arguments: ", args)

# plotting the graph
plt.plot(values_x, values_y, "bo", label="y - original")
plt.plot(values_x, y_fit1, label="y = a * x^2 + b * x + c")
plt.plot(values_x, y_fit2, label="y = b * x^a + c")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best", fancybox=True, shadow=True)
plt.grid(True)
plt.show()

# https://pythonpip.ru/examples/podgonka-krivoy-v-python-s-pomoschyu-biblioteki-scipy
