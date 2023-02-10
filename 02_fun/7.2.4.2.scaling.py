import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
N, D = X.shape
print((.5 * np.eye(N)) @ X)
print(X @ (np.eye(D) * .5))
