import numpy as np
import matplotlib.pyplot as plt

def sigmoid(a, t):
	return 1 / (1 + np.exp(-(a-t)))

a = np.linspace(-5, 9, 200)
plt.figure()
plt.plot(a, sigmoid(a, 2), linewidth=2)
plt.grid(True)
plt.axis([-5, 9, -0.02, 1.02])
plt.xticks(np.arange(-5, 10, step=1))
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.show()
