import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
N, D = X.shape
print(np.ones(N) @ X)
print(X @ np.ones(D))
print(np.ones(N) @ X @ np.ones(D))
print(np.mean(X, axis=0))
print(np.mean(X))
