import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_r2(X, Y):
    w = np.linalg.solve( X.T.dot(X), X.T.dot(Y) )
    Yhat = X.dot(w)

    d1 = Y - Yhat
    d2 = Y - Y.mean()
    r2 = 1 - d1.dot(d1) / d2.dot(d2)
    return r2

# Using pandas
df = pd.read_csv('data_1d.csv', header=None)
df.columns = ['x', 'y']
df['1'] = 1

# Turning X and Y into numpy arrays
X = df['x'].as_matrix()
X1 = df[['1','x']].as_matrix()
Y = df['y'].as_matrix()

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

# # Calculate R-squared
# d1 = Y - Yhat
# d2 = Y - Y.mean()
# r2 = 1 - d1.dot(d1) / d2.dot(d2)
# print("The R-squared is %s" % r2)
print("The R-squared is %s" % get_r2(X1, Y))