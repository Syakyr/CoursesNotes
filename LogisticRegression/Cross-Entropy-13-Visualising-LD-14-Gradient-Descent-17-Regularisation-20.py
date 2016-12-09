#################################################
#   Cross-Entropy, Linear Discriminant (Bayes   #
#   Identtifier), Gradient Descent and          #
#   Regularisation                              #
#################################################

import numpy as np
import matplotlib.pyplot as plt

N = 100
D = 2

# Sigmoid Function
def sigmoid(z):
    return 1/(1 + np.exp(-z))

# Cross Entropy Error Function
def cross_entropy(T, Y):
    E = 0
    for i in range(N):
        if T[i] == 1:
            E -= np.log(Y[i])
        else:
            E -= np.log(1-Y[i])
    return E

# Create 2 Gaussian clouds of 100 samples , X[i] = (x1.i, x2.i)
X = np.random.randn(N,D)

# Center the 1st 50 points at (-2,-2)
X[:50, :] = X[:50, :] - 2*np.ones((50,D))
# Center the last 50 points at (2, 2)
X[50:, :] = X[50:, :] + 2*np.ones((50,D))

# Labels: First 50 are 0, last 50 are 1
T = np.array([0]*50 + [1]*50)

# Add a column of ones into X --> Xb[i] = (1, x1.i, x2.i)
ones = np.array([[1]*N]).T
Xb = np.concatenate((ones, X), axis=1)

### First Instance: Using random weights ###
# randomly initialise the weights
w1 = np.random.randn(D + 1)

# calculate the model output and the sigmoid
z = Xb.dot(w1)
Y = sigmoid(z)
print(cross_entropy(T, Y))

### Second Instance: Using the Closed-Form Solution
w2 = np.array([0, 4, 4])

z = Xb.dot(w2)
Y = sigmoid(z)
print(cross_entropy(T, Y))

# # Plot y = -x
# x_axis = np.linspace(-6, 6, 100)
# y_axis = -1 * x_axis
# plt.plot(x_axis, y_axis)
#
# plt.scatter(X[:,0], X[:,1], c=T, s=N, alpha=0.5)
#
# plt.show()

### Third Instance: Using Gradient Descent

w3 = w1.copy()

learning_rate = 0.1
for i in range(100):
    if i % 10 == 0:
        print (cross_entropy(T, Y))

    w3 += learning_rate * (T-Y).T.dot(Xb)
    Y = sigmoid(Xb.dot(w3))

print("Final w: %s" % w3)

### Fourth Instance: Using Gradient Descent with regularisation

w4 = w1.copy()

learning_rate = 0.1
for i in range(100):
    if i % 10 == 0:
        print (cross_entropy(T, Y))

    w4 += learning_rate * ((T-Y).T.dot(Xb) - 0.1*w4)
    Y = sigmoid(Xb.dot(w4))

print("Final w: %s" % w4)