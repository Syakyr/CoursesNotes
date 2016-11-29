import numpy as np
import time

#####################################################
# Lecture 8 - Matrix Products & Other Operations    #
#####################################################

def TimeElapsed(ID, function):
    start = time.perf_counter()
    print("Method %s:" % ID)
    calc = function
    elapsed = time.perf_counter() - start
    print("Answer is %s, elapsed in %s seconds\n" % (calc, elapsed))
    return elapsed

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("A = \n%s\nB = \n%s\n" % (A,B))

# Element-Wise Multiplication:
print("A ⊙ B = \nA * B = \n%s\n" % (A*B))
print("B ⊙ A = \nB * A = \n%s\n" % (B*A))   # Commutative, unlike Matrix Multiplication

# Matrix Multiplication:
print("A  ×  B  = \nA.dot(B) = \n%s\n" % (A.dot(B)))
print("B  ×  A  = \nB.dot(A) = \n%s\n" % (B.dot(A)))

# Inverse Function:
print("A^(-1)           = \nnp.linalg.inv(A) = \n%s\n" % (np.linalg.inv(A)))
# You can shorten the function by passing it to another name:
inv = np.linalg.inv
print("Passing 'np.linalg.inv' to 'inv'")
print("A^(-1) = \ninv(A) = \n%s\n" % (inv(A)))

# Determinant Function:
print("det(A)           = \nnp.linalg.det(A) = \n%s\n" % (np.linalg.det(A)))
# You can shorten the function by passing it to another name:
det = np.linalg.det
print("Passing 'np.linalg.det' to 'det'")
print("det(A) = \n%s\n" % (det(A)))

# Diagonal function
# 2 functions depending on the type of array,
# 2-D array gives a 1-D array from the diagonal entries
# 1-D array gives a 2-D array as a diagonal matrix
print("np.diag(A) = %s" % np.diag(A))
print("np.diag(np.diag(A)) = \n%s\n" % np.diag(np.diag(A)))

# TODO: Continue where I left off (traces and eigenvalues/vectors).