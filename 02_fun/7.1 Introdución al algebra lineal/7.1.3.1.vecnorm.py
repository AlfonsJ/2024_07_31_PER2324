import numpy as np
a = np.array([-3, 4])
print(np.linalg.norm(a, 1))
print(np.linalg.norm(a, 2))
print(np.linalg.norm(a, np.inf))
