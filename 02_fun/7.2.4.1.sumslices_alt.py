import numpy as np
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ])
print(np.sum(X, axis=0, dtype=float))
print(np.sum(X, axis=1, dtype=float))
print(np.sum(X, dtype=float))
# print(np.add.reduce(X, 0, dtype=float))
# print(np.add.reduce(X, 1, dtype=float))
# print(np.add.reduce(X, (0, 1), dtype=float))
