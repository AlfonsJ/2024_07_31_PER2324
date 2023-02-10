import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
S0 = X.T @ X
print(S0)
N, D = X.shape
Sx = np.cov(X, rowvar=False, bias=True)
print(N*Sx)
