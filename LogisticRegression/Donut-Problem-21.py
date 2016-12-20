import numpy as np
import matplotlib.pyplot as plt

N = 1000
N_half = int(N / 2)
D = 2

R_inner = 5
R_outer = 10

R1 = np.random.randn(N_half) + R_inner
theta = 2 * np.pi * np.random.random(N_half)
X_inner = np.concatenate([[R1 * np.cos(theta)], [R1 * np.sin(theta)]]).T

R2 = np.random.randn(N_half) + R_outer
theta = 2 * np.pi * np.random.random(N_half)
X_outer = np.concatenate([[R2 * np.cos(theta)], [R2 * np.sin(theta)]]).T

X = np.concatenate([X_inner, X_outer])
T = np.array([0]*int(N_half) + [1]*int(N_half))

plt.scatter(X[:,0], X[:,1], c = T)
plt.show()

ones = np.array([[1]*N]).T

r = np.zeros((N,1))

for i in range(N):
    r[i] = np.sqrt(X[i,:].dot(X[i,:]))

Xb = np.concatenate((ones, r, X), axis=1)

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

learning_rate = 0.0001
error = []
for i in range(5000):
    e = cross_entropy(T, Y)
    error.append(e)
    # if i % 100 == 0:
    #     print ("%d: %f" % (i, e))

    w += learning_rate * ((T-Y).T.dot(Xb) - 0.1*w)
    Y = sigmoid(Xb.dot(w))

# plt.plot(error)
# plt.title("Cross-entropy")
# plt.show()

print("Final w: %s" % w)
print("Final classification rate: %.05f" % (1 - np.abs(T - Y.round()).sum() / N))