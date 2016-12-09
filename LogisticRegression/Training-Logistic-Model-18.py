import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from process_08 import get_binary_data

# Loads the data and shuffles them
X, Y = get_binary_data()
X, Y = shuffle(X,Y)

# Divides the data with train and test sets
Xtrain = X[:-100]
Ytrain = Y[:-100]
Xtest = X[-100:]
Ytest = Y[-100:]

# Creates the Gaussian-distributed weight and bias term
D = X.shape[1]
print (X.shape)
W = np.random.randn(D)
b = 0

# Sigmoid function
def sigmoid(z): # Gives a value between 0 and 1
    return 1 / (1 + np.exp(-z))

# Feed forward function
def forward(X, W, b): # See P_Y_given_X
    return sigmoid(X.dot(W) + b)

# How accurate is the classification prediction given we already have the answer that is Y
def classification_rate(Y, P):
    return np.mean(Y == P)

# Cross entropy function
def cross_entropy(T, pY):
    return (-np.mean(T*np.log(pY) - (1 - T)*np.log(1 - pY)))

# Begin testing (without regularisation from lesson 20)
train_costs = []
test_costs  = []
learning_rate = 0.001
for i in range(10000):
    pYtrain = forward(Xtrain, W, b)
    pYtest = forward(Xtest, W, b)

    ctrain = cross_entropy(Ytrain, pYtrain)
    ctest  = cross_entropy(Ytest, pYtest)
    train_costs.append(ctrain)
    test_costs.append(ctest)

    W -= learning_rate * Xtrain.T.dot(pYtrain - Ytrain)
    b -= learning_rate * (pYtrain - Ytrain).sum()
    if i % 1000 == 0:
        print("%i: %f, %f" % (i, ctrain, ctest))

print ("Final train classification rate: %f" % classification_rate(Ytrain, pYtrain.round()))
print ("Final test classification rate: %f"  % classification_rate(Ytest, pYtest.round()))

legend1, = plt.plot(train_costs, label='train cost')
legend2, = plt.plot(test_costs,  label='test cost')
plt.legend([legend1, legend2])

plt.show()