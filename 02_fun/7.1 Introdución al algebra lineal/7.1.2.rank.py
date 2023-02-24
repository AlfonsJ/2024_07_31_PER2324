import numpy as np
A = np.eye(4)
print(np.linalg.matrix_rank(A))
A[-1, -1] = 0.
print(np.linalg.matrix_rank(A))
A = np.ones((4,))
print(np.linalg.matrix_rank(A))
A = np.zeros((4,))
print(np.linalg.matrix_rank(A))
