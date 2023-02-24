import numpy as np
import matplotlib.pyplot as plt
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
m = np.mean(X, axis=0)
fig, ax = plt.subplots()
ax.set_aspect("equal")
plt.grid(True)
plt.axis([-2, 4, -2, 4])
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.scatter(m[0], m[1], facecolor='C0', edgecolor='k',
	s=100, marker="X")
plt.scatter(X[:,0], X[:,1], facecolor='C0', edgecolor='k',
	s=100)
plt.savefig("7.2.4.plotX.eps")
