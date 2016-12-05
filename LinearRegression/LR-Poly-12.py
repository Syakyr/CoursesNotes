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

# With pandas
df = pd.read_csv('data_poly.csv', header=None)
df.columns = ['x','y']
df['x^2'] = df.apply(lambda row: row['x']**2, axis=1)
df['x^0'] = 1

X0 = df[['x^0','x']].as_matrix()
X = df[['x^0','x','x^2']].as_matrix()
Y = df['y'].as_matrix()

# # Without pandas, as per the lesson
# X = []
# Y = []
# for line in open('data_poly.csv'):
#     x, y = line.split(',')
#     x = float(x)
#     X.append([1, x, x**2])
#     Y.append(float(y))
#
# # Convert to numpy arrays
# X = np.array(X)
# Y = np.array(Y)

# Plot the scatter
plt.scatter(X[:,1], Y)
plt.show()

# Calculate the weights
w = np.linalg.solve(X.T.dot(X), X.T.dot(Y))
Yhat = X.dot(w)
w0 = np.linalg.solve(X0.T.dot(X0), X0.T.dot(Y))
Yhat0 = X0.dot(w0)

# Plot it again
plt.scatter(X[:,1], Y)
plt.plot(sorted(X[:,1]), sorted(Yhat))
plt.plot(X0[:,1], Yhat0)
plt.show()

# # Compute R^2
# d1 = Y - Yhat
# d2 = Y - Y.mean()
# r2 = 1 - d1.dot(d1) / d2.dot(d2)
# print("The R^2 is %s" % r2)
print("The R^2 (without quadratic) is %s" % get_r2(X0, Y))
print("The R^2 (with quadratic) is %s" % get_r2(X, Y))
