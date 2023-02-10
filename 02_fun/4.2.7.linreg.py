import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 1.0, 1.0, 2.0])
A = np.vstack([x, np.ones(len(x))]).T
y = np.array([0.0, 0.5, 1.5, 2.0])
[m, c], [r], _, _ = np.linalg.lstsq(A, y, rcond=None)

print(np.around(m,2), np.around(c,2), np.around(r,2))

plt.plot(x, y, 'o', markersize=10)
plt.plot(x, m*x + c, 'r')
plt.grid(True)
plt.show()
