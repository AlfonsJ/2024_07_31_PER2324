import numpy as np
A = np.array([ [5/2, 3/2], [3/2, 5/2] ])
L, E = np.linalg.eigh(A)
print(L, "\n", E, "\n")
U, S, Vt = np.linalg.svd(A)
print(U, "\n", S, "\n", Vt)
