import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
Xs = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
print(Xs)
### plots
import matplotlib.pyplot as plt
m = np.mean(X, axis=0)
s = np.std(X, axis=0)

# plot A
fig, ax = plt.subplots()
ax.set_aspect("equal")
plt.grid(True)
plt.axis([-2, 4, -2, 4])
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.scatter(m[0], m[1], facecolor='C0', edgecolor='k', s=100, marker="X")
prop = dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
            shrinkA=0, shrinkB=0)
plt.annotate("", xytext=(m[0], m[1]), xy=(m[0]+s[0], m[1]), arrowprops=prop)
plt.annotate("", xytext=(m[0], m[1]), xy=(m[0], m[1]+s[1]), arrowprops=prop)
plt.scatter(X[:,0], X[:,1], facecolor='C0', edgecolor='k', s=100)
plt.savefig("7.4.5.standardize_A.eps")

# plot B
fig, ax = plt.subplots()
ax.set_aspect("equal")
plt.grid(True)
plt.axis([-2, 2, -2, 2])
plt.xticks(np.arange(-2, 3, step=1), fontsize=16)
plt.yticks(fontsize=16)
plt.yticks(np.arange(-2, 3, step=1), fontsize=16)
plt.scatter(0, 0, facecolor='C1', edgecolor='k', s=100, marker="X")
prop['color'] = 'C1'
plt.annotate("", xytext=(0, 0), xy=(1, 0), arrowprops=prop)
plt.annotate("", xytext=(0, 0), xy=(0, 1), arrowprops=prop)
plt.scatter(Xs[:,0], Xs[:,1], facecolor='C1', edgecolor='k', s=100)
plt.savefig("7.4.5.standardize_B.eps")

# plt.show()
