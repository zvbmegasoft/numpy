import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 4, 10)
y = 3 * x**3 - 13 * x**2 + 12 * x - 3
plt.title = "График функции"
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
