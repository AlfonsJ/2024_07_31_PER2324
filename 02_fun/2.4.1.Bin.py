import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

N, t = 10, 0.2
S = binom(N, t)
s = np.arange(N+1)
print(s, S.pmf(s), S.rvs(10))
plt.bar(s, S.pmf(s))
plt.show()
