import numpy as np
import matplotlib.pyplot as plt

def logit(p):
	return np.log(p / (1 - p))

p = np.linspace(.001, .999, 200)
plt.figure()
plt.plot(p, logit(p), linewidth=2)
plt.grid(True)
plt.axis([-0.02, 1.02, -5, 5])
plt.xticks(np.arange(0, 1.1, step=0.1))
plt.yticks(np.arange(-5, 6, step=1))
plt.show()
