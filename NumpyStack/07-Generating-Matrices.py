import numpy as np
import time

###################################
# Lecture 7 - Generating Matrices #
###################################

def TimeElapsed(ID, function):
    start = time.perf_counter()
    print("Method %s:" % ID)
    calc = function
    elapsed = time.perf_counter() - start
    print("Answer is %s, elapsed in %s seconds\n" % (calc, elapsed))
    return elapsed

# Creating a zero vector of size 10
Z = np.zeros(10)
print("Z = %s\n" % Z)

# Creating a zero matrix of size 10 by 10
Z = np.zeros((10, 10))
print("Z = \n%s\n" % Z)

# Creating a 'ones' matrix of size 10 by 10
O = np.ones((10, 10))
print("O = \n%s\n" % O)

# Creating a matrix of random numbers
# between 0 and 1 of size 10 by 10
R = np.random.random((10, 10))
print("R = \n%s\n" % R)

# Creating a matrix of normally distributed
# numbers between 0 and 1 of size 10 by 10
G = np.random.randn(10, 10) # Take note of the lack of extra brackets
print("G = \n%s\n" % G)

# Mean and Variance of G
print("Mean of G = %s\nVariance of G = %s" % (G.mean(), G.var()))