import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = pd.read_csv('data_1d.csv', header=None).as_matrix()

# Histogram Data
x = A[:,0]
y = A[:,1]

# Create histogram with data x
plt.hist(x)
plt.show()

# Create histogram with random sample of 10000
random = np.random.random
R = random(10000)
plt.hist(R, bins=20) # Creates 20 buckets of data
plt.show()

# Finding the variance from the best fit line
y_actual = 2*x + 1
residuals = y - y_actual

plt.hist(residuals)
plt.show()