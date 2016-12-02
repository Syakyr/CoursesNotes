import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Using pandas
A = pd.read_csv('data_1d.csv', header=None)

# Turning X and Y into numpy arrays
X = A[0].as_matrix()
Y = A[1].as_matrix()

# # Plot the values X and Y
# plt.scatter(X, Y)
# plt.show()


# # W/o using pandas, as per the lesson
# del X, Y
# X = []
# Y = []
# for line in open('data_1d.csv'):
#     x, y = line.split(',')
#     X.append(float(x))
#     Y.append(float(y))
#
# X = np.array(X)
# Y = np.array(Y)
#
# plt.scatter(X, Y)
# plt.show()

# Apply linear regression by its original calculation
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

# Calculate predicted Y
Yhat = a*X + b

# Plot them again
plt.scatter(X, Y)
plt.plot(X, Yhat)
plt.show()

# Calculate R-squared
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)
print("The R-squared is %s" % r2)