import numpy as np

def load_reg1d(N=21, random_state=0):
    np.random.seed(random_state)
    X_train = np.linspace(0.0, 20, N)
    X_test = np.arange(0.0, 20, 0.1)
    w0 = 0
    w1 = -1.5
    w2 = 1/9
    sigma = 2
    y_train = w0 + w1 * X_train + w2 * X_train * X_train + np.random.normal(0, sigma, X_train.shape)
    y_test = w0 + w1 * X_test + w2 * X_test * X_test + np.random.normal(0, sigma, X_test.shape)
    return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)
