#!/usr/bin/env python
import numpy as np
import time

def TimeElapsed(ID, function):
    start = time.perf_counter()
    print("Method %s:" % ID)
    calc = function
    elapsed = time.perf_counter() - start
    print("Answer is %s, elapsed in %s seconds\n" % (calc, elapsed))
    return elapsed

###################################
# Lecture 3 - Lists vs Arrays     #
###################################
print("~~~ Lecture 3 - Lists vs Arrays ~~~\n")

L = [1,2,3]
print("L = [1,2,3]")
A = np.array([1,2,3])
print("A = np.array([1,2,3])\n")

# What both lists and arrays can do:
print("What both lists and arrays can do:")
# Reiteration of for loops
print("Reiteration of for loops\n")

def loop(list):
    for e in list:
        print(e)

print ('Loop of list:')
elapsed1 = TimeElapsed(1,loop(L))

print ('Loop of array:')
loop(A)
elapsed2 = TimeElapsed(2,loop(A))

# Speed Factor
factor = elapsed1/elapsed2
print ("Method 2 is %s faster than Method 1" % factor)

print("")

# What only lists can do:
print("What only lists can do:")

# Appends
print("Appends: L.append(4)")
L.append(4)
print(L)

# Concaternate
print("Concaternate: L+=[5]")
L+=[5]
print(str(L) + "\n")

# Numpy Arrays cannot append nor it can add more elements like how lists can be done
print("Append on A will get an error like this:")
print("AttributeError: \'numpy.ndarray\' object has no attribute \'append\'\n")

# Differences
print("Differences:\n")
print("Addition of lists will get this:")
print("L + L = " + str(L+L) + "\n")
print("Addition of arrays will get this:")
print("A + A = " + str(A+A) + "\n")

print("Same with multiplication:")
print("2 * L = " + str(2*L))
print("2 * A = " + str(2*A) + "\n")

print("For multiplication on lists, you need to do a for loop:\n")

# For multiplication on lists
L1 = [1,2,3]
def listmultiply():
    L2 = []
    for e in L1:
        L2.append(e + e)
    return L2

elapsed1 = TimeElapsed(1,listmultiply())
print ("Elapsed in %s seconds for list loop\n" % elapsed1)

# For multiplication on arrays
elapsed2 = TimeElapsed(2,2*A)

# Speed Factor
factor = elapsed1/elapsed2
print ("Method 2 is %s faster than Method 1" % factor)

