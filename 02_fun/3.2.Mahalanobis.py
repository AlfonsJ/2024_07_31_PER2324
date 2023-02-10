import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

U = np.array([[.71, -.71], [.71, .71]])
La = np.array([3.8, .2])
r = 2.45
t = np.linspace(0, 2*np.pi, 100)
x, y = U @ np.diag(np.sqrt(La)) @ np.array([r*np.cos(t), r*np.sin(t)])
Y = np.vstack((x, y)).T
cov = U @ np.diag(La) @ U.T
X = multivariate_normal(cov=cov).rvs(100)
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
plt.plot(Y[:, 0], Y[:, 1])
plt.scatter(X[:,0],X[:,1])
plt.show()
