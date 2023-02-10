import numpy as np
import matplotlib.pyplot as plt

def sigmoid(a):
	return 1 / (1 + np.exp(-a))

def softplus(a):
	return np.log(1 + np.exp(-a))

a = np.linspace(-5, 5, 200)
plt.figure()
plt.plot(a, softplus(a), linewidth=2)
plt.grid(True)
plt.axis([-5, 5, -0.02, 5.2])
plt.xticks(np.arange(-5, 6, step=1))
#plt.yticks(np.arange(0, 1.1, step=0.1))
plt.show()
