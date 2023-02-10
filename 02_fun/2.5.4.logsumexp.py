import numpy as np
from scipy.special import logsumexp

a = 1.0 * np.array([0, 1, 0])
print(np.log(np.sum(np.exp(a))), logsumexp(a))

a = 1.0 * np.array([1000, 1001, 1000])
print(np.log(np.sum(np.exp(a))), logsumexp(a))

a = 1.0 * np.array([-1000, -999, -1000])
print(np.log(np.sum(np.exp(a))), logsumexp(a))
