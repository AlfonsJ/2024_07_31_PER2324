from scipy.stats import bernoulli
import matplotlib.pyplot as plt

t = 0.2
Y = bernoulli(t)
y = [0, 1]
print(y, Y.pmf(y), Y.rvs(10))
plt.bar(y, Y.pmf(y), width=0.1)
plt.show()
