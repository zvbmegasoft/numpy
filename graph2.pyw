import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 1, 1000)
y = x - np.cos(x)
plt.title = "График функции"
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
