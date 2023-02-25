import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 5, 50)
y = 2 * np.exp(1 - x) - 3.5 * np.sin(x)
plt.title = "График функции"
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
