import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

# Using pandas
Moore = pd.read_csv("moore.csv", header=None, sep='\t')

non_decimal = re.compile(r'[^\d]+')

Moore[6] = Moore.apply(lambda row: int(non_decimal.sub('', row[2].split('[')[0])), axis=1)
Moore[7] = Moore.apply(lambda row: int(non_decimal.sub('', row[1].split('[')[0])), axis=1)

X = np.array(Moore[6])
Y = np.array(Moore[7])

# # Without using pandas, as per the lesson
# X = []
# Y = []
#
# non_decimal = re.compile(r'[^\d]+')
#
# for line in open('moore.csv'):
#     r = line.split('\t')
#
#     # Removes Wikipedia entry:
#     x = int(non_decimal.sub('', r[2].split('[')[0]))
#     y = int(non_decimal.sub('', r[1].split('[')[0]))
#     X.append(x)
#     Y.append(y)
#
# X = np.array(X)
# Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

Y = np.log(Y)
plt.scatter(X, Y)
plt.show()

# Apply linear regression by its original calculation
denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot (Y) - Y.mean() * X.sum() ) / denominator
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
print ("a = %s, b = %s" % (a, b))
print("The R^2 is %s" % r2)

### tc = transistor count, p1 = period 1,
### p2 = period 2
# log (tc) = a*p1 + b
# tc = exp(b) * exp(a*p1)
# 2*tc = exp(ln(2)) * exp(b) * exp(a*p1)
#      = exp(b) * exp(a*p1 + ln(2))
# exp(b) * exp(a*p2) = exp(b) * exp(a*p1 + ln(2))
#          exp(a*p2) = exp(a*p1 + ln(2))
#              a*p2  = a*p1 + ln(2)
#                p2  = p1 + ln(2)/a
print('Time to double is in %f years' % (np.log(2)/a))