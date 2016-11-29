import numpy as np
import time

###################################
# Lecture 4 - Dot Product         #
###################################

def TimeElapsed(ID, function):
    start = time.perf_counter()
    print("Method %s:" % ID)
    calc = function
    elapsed = time.perf_counter() - start
    print("Answer is %s, elapsed in %s seconds\n" % (calc, elapsed))
    return elapsed

### Array initialisation ###
print("Array initialisation:")
a = np.array([1,2])
b = np.array([2,1])
print("a = np.array([1,2])\n\
b = np.array([2,1])\n")

### Dot Product ###
print("Dot product of a and b:\n")

# Method 1 for getting the dot product a.b
def dotproduct1():
    dot = 0
    for e, f in zip(a, b):
        dot += e*f
    return dot
elapsed1 = TimeElapsed(1, dotproduct1())

# Method 2
elapsed2_1 = TimeElapsed(2.1, np.sum(a*b))
elapsed2_2 = TimeElapsed(2.2, (a*b).sum())
elapsed2   = (elapsed2_1+elapsed2_2)/2

# Method 3
elapsed3_1 = TimeElapsed(3.1, a.dot(b))
elapsed3_2 = TimeElapsed(3.2, b.dot(a))
elapsed3   = (elapsed3_1+elapsed3_2)/2

# Speed Factor
factor21   = elapsed1/elapsed2
factor31   = elapsed1/elapsed3
print("Method 2 is %s faster than Method 1" % factor21)
print("Method 3 is %s faster than Method 1" % factor31)

print("")

### Vector Length ###
print("Vector Length of a:\n")

# Method 1
elapsed1 = TimeElapsed(1, np.sqrt((a*a).sum()))

# Method 2
elapsed2 = TimeElapsed(2, np.linalg.norm(a))

# Speed Factor
factor21 = elapsed1/elapsed2
print("Method 2 is %s faster than Method 1" % factor21)
print("")

### Angle between 2 Vectors ###
print("Angle between a and b:\n")

def anglecalc(method):
    cosangle = a.dot(b) / method
    angle = np.arccos(cosangle)
    return angle

# Method 1 - using Method 1 of Vector Length
elapsed1 = TimeElapsed(1,anglecalc(np.sqrt((a*a).sum()) * np.sqrt((b*b).sum())))

# Method 2 - using Method 2 of Vector Length
elapsed2 = TimeElapsed(2,anglecalc(np.linalg.norm(a) * np.linalg.norm(b)))

# Speed Factor
factor21 = elapsed1/elapsed2
print("Method 2 is %s faster than Method 1" % factor21)
