import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)   # Plot x from 0 to 10 with 100 points
y = np.sin(x)               # y as a function of x
plt.plot(x,y)               # Plot y against x
plt.title("f(t) against t") # Title of the graph
plt.xlabel("t")             # x label
plt.ylabel("f(t)")          # y label
plt.show()                  # Render the graph