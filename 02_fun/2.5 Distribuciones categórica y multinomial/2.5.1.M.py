import numpy as np
from scipy.stats import multinomial
import matplotlib.pyplot as plt

N, t = 10, [0.3, 0.2, 0.5]
S = multinomial(N, t)
print(S.pmf([3, 2, 5]))
print(S.rvs(4))
plt.bar(np.arange(1,len(t)+1), S.p)
plt.show()
