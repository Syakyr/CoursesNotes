import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('mlr02.xls')
X = df.as_matrix()

plt.scatter(X[:,1], X[:,0])
plt.show()

plt.scatter(X[:,2], X[:,0])
plt.show()

df['ones'] = 1
Y = df['X1']
X = df[['X2', 'X3', 'ones']]
X2only = df[['X2', 'ones']]
X3only = df[['X3', 'ones']]

def get_r2(X, Y):
    w = np.linalg.solve( X.T.dot(X), X.T.dot(Y) )
    Yhat = X.dot(w)

    d1 = Y - Yhat
    d2 = Y - Y.mean()
    r2 = 1 - d1.dot(d1) / d2.dot(d2)
    return r2

print("r2 for x2 only: %s" % get_r2(X2only, Y))
print("r2 for x3 only: %s" % get_r2(X3only, Y))
print("r2 for x: %s" % get_r2(X, Y))