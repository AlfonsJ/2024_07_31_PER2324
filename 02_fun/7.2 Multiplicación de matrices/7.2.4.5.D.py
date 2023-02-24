import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ], dtype=float)
N, D = X.shape
K = X.dot(X.T)
H = np.tile(np.diag(K), (N, 1))
print(H + H.T - 2*K)
