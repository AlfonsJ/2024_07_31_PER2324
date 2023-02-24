import numpy as np
A = np.array([[2, 1], [1, 2]])
print(np.trace(A))
print(round(np.linalg.det(A)))
print(np.linalg.matrix_rank(A))
print(round(np.linalg.cond(A)))
