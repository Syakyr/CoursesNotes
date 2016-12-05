import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def get_r2(X, Y):
    w = np.linalg.solve( X.T.dot(X), X.T.dot(Y) )
    Yhat = X.dot(w)

    d1 = Y - Yhat
    d2 = Y - Y.mean()
    r2 = 1 - d1.dot(d1) / d2.dot(d2)
    return r2

# With pandas
df = pd.read_csv('data_2d.csv', header=None)
df[3] = 1

X = A[[0,1,3]].as_matrix()
Y = A[2].as_matrix()

# # Without pandas, as per the lesson
# X = []
# Y = []
# for line in open('data_2d.csv'):
#     x1, x2, y = line.split(',')
#     X.append([float(x1), float(x2),1])
#     Y.append(float(y))
#
# # Turn X and Y into numpy arrays
# X = np.array(X)
# Y = np.array(Y)

# Plot the data
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], Y)
plt.show()

# Calculate weights
w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
Yhat = X.dot(w)

# # Compute R^2
# d1 = Y - Yhat
# d2 = Y - Y.mean()
# r2 = 1 - d1.dot(d1) / d2.dot(d2)
# print("The R^2 is %s" % r2)
print("The R^2 is %s" % get_r2(X,Y))
