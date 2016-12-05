import numpy as np
from process_08 import get_binary_data

X, Y = get_binary_data()

D = X.shape[1] # Number of columns of X
W = np.random.randn(D) # Assumes random Gaussian distribution as the weight in linreg
b = 0 # bias term set to 0

def sigmoid(z): # Gives a value between 0 and 1
    return 1 / (1 + np.exp(-z))

def forward(X, W, b): # See P_Y_given_X
    return sigmoid(X.dot(W) + b)

P_Y_given_X = forward(X, W, b) # The probability of Y is true given input of X
predictions = np.round(P_Y_given_X)

# How accurate is the classification prediction given we already have the answer that is Y
def classification_rate(Y, P):
    return np.mean(Y == P)

print ("Score is %f" % classification_rate(Y, predictions))

# Score is not accurate since W is random from Gaussian distribution, not from linreg