import numpy as np
import matplotlib.pyplot as plt

N = 4
D = 2

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])
T = np.array([0, 1, 1, 0])

ones = np.ones((N, 1))

xy = np.matrix(X[:,0] * X[:,1]).T

Xb = np.array(np.concatenate((ones, xy, X), axis=1))

w = np.random.randn(D+2)

z = Xb.dot(w)

# Sigmoid Function
def sigmoid(z):
    return 1/(1 + np.exp(-z))

Y = sigmoid(z)

# Cross Entropy Error Function
def cross_entropy(T, Y):
    E = 0
    for i in range(N):
        if T[i] == 1:
            E -= np.log(Y[i])
        else:
            E -= np.log(1-Y[i])
    return E

learning_rate = 0.001
error = []
for i in range(5000):
    e = cross_entropy(T, Y)
    error.append(e)
    # if i % 100 == 0:
    #     print ("%d: %f" % (i, e))

    w += learning_rate * ((T-Y).T.dot(Xb) - 0.01*w)
    Y = sigmoid(Xb.dot(w))

# plt.plot(error)
# plt.title("Cross-entropy")
# plt.show()

print("Final w: %s" % w)
print("Final classification rate: %.05f" % (1 - np.abs(T - Y.round()).sum() / N))