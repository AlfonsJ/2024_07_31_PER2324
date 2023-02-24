import numpy as np
import scipy.spatial as spt
X = np.array([ [-1, -1], [0, 2], [2, 0], [3, 3] ], dtype=float)
V = spt.distance.pdist(X, 'sqeuclidean')
print(spt.distance.squareform(V))
