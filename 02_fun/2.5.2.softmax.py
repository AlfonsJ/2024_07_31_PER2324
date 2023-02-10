import numpy as np
import matplotlib.pyplot as plt

def softmax(a):
	e = np.exp((1.0 * np.array(a)))
	return e / np.sum(e)

a = np.array([3, 0, 1])
plt.bar(np.arange(1,a.size+1), softmax(a))
plt.show()
