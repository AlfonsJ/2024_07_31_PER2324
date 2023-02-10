import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

m, v = 0.0, 1.0
Y = norm(m, v)
y = np.linspace(-3, 3, 200)
plt.plot(y, Y.pdf(y))
plt.show()
