import numpy as np
a = np.arange(8)
print(a, a.shape)
a2d = a.reshape([2, -1])
print(a2d, a2d.shape)
a3d = a.reshape([2, 2, -1])
print(a3d, a3d.shape)
