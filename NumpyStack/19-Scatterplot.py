import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = pd.read_csv('data_1d.csv', header=None).as_matrix()

# Scatter plot Data
x = A[:,0]
y = A[:,1]

# Best fit line (defined by lazyprogrammer)
x_line = np.linspace(0, 100, 100)
y_line = 2*x_line + 1

# Show the scatter plot and best fit line
plt.scatter(x,y)
plt.plot(x_line, y_line)
plt.show()
