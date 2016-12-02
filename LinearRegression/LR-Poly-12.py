import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Without pandas, as per the lesson
X = []
Y = []
for line in open('data_poly.csv'):
    x, y = line.split(',')
    x = float(x)
    X.append([1, x, x**2])
    Y.append(float(y))

# Convert to numpy arrays
X = np.array(X)
Y = np.array(Y)

# Plot the scatter
plt.scatter(X[:,1], Y)
plt.show()

# Calculate the weights
w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
Yhat = X.dot(w)

# Plot it again
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Yhat))
plt.show()

# Compute R^2
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("The R^2 is %s" % r2)
