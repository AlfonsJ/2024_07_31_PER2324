import numpy as np
S = np.array([[2, 1.8], [1.8, 2]])
La, U = np.linalg.eigh(S)
i = La.argsort()[::-1]; La = La[i]; U = U[:,i]
print(La, U, U @ np.diag(La) @ U.T)
