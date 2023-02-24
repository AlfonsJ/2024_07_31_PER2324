import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
m = np.mean(X, axis=0)
S = np.cov(X.T, bias=True)
La, U = np.linalg.eigh(S)
i = La.argsort()[::-1]; La = La[i]; U = U[:,i]
W = np.sqrt(np.linalg.inv(np.diag(La))) @ U.T
Xw = (X - m) @ W.T
print(W, Xw)
A = U @ np.diag(np.sqrt(La))
### plots
import matplotlib.pyplot as plt
s = np.std(X, axis=0)

# plot A
fig, ax = plt.subplots()
ax.set_aspect("equal")
plt.grid(True)
plt.axis([-2, 4, -2, 4])
plt.xticks(np.arange(-2, 5, step=1), fontsize=16)
plt.yticks(fontsize=16)
plt.scatter(m[0], m[1], facecolor='C0', edgecolor='k', s=100, marker="X")
prop = dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
            shrinkA=0, shrinkB=0)
plt.annotate("", xytext=(m[0], m[1]), xy=(m[0]+A[0,0], m[1]+A[1,0]),
						 arrowprops=prop)
plt.annotate("", xytext=(m[0], m[1]), xy=(m[0]+A[0,1], m[1]+A[1,1]),
						 arrowprops=prop)
plt.scatter(X[:,0], X[:,1], facecolor='C0', edgecolor='k', s=100)
plt.scatter(X[:,0], X[:,1], facecolor='C0', edgecolor='k', s=100)
plt.savefig("7.4.5.pca_A.eps")

# plot B
fig, ax = plt.subplots()
ax.set_aspect("equal")
plt.grid(True)
plt.axis([-2, 4, -2, 4])
plt.xticks(np.arange(-2, 5, step=1), fontsize=16)
plt.yticks(fontsize=16)
prop['color']='C1'
plt.scatter(0, 0, facecolor='C1', edgecolor='k', s=100, marker="X")
plt.annotate("", xytext=(0,0), xy=(1,0), arrowprops=prop)
plt.annotate("", xytext=(0,0), xy=(0,1), arrowprops=prop)
plt.scatter(Xw[:,0], Xw[:,1], facecolor='C1', edgecolor='k', s=100)
plt.savefig("7.4.5.pca_B.eps")
