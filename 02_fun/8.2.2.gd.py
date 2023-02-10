import numpy as np
grad, theta, eta, tol = lambda t: 2*t, 10.0, 0.2, 0.01
while True:
	delta = -eta * grad(theta)
	if np.all(np.abs(delta) <= tol):
		break
	theta += delta
	print(round(theta, 3))
