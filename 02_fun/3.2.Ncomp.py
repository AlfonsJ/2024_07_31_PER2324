import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

m, S = [0, 0], [[2, 1.8], [1.8, 2]]
x, y = np.mgrid[-5:5:.1, -5:5:.1]
z = multivariate_normal(m, S).pdf(np.dstack((x, y)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='white', edgecolor="black")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111,aspect='equal')
ax.contour(x, y, z)
plt.show()
