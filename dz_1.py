import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-10, 10, 0.01)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(2 * x))
plt.show()

