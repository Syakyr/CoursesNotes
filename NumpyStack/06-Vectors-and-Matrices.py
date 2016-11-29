import numpy as np

###################################
# Lecture 6 - Vectors & Matrices  #
###################################

# Arrays and Lists can be created as Matrices as well.
M = np.array([[1,2],[3,4]])
L = [[1,2],[3,4]]

print('L[0] = %s\n' % L[0])
print('L[0][0] = %s\n' % L[0][0])

# Matrix entries can be written in Matlab style as well
print('M[0][0] = %s\n' % M[0][0])
print('M[0,0] = %s\n' % M[0,0])

# You can pass a matrix using np.matrix as well,
# but it's NOT recommended.
M2 = np.matrix([[1,2],[3,4]])
print("M2 = \n%s\n" % M2)

# You can convert np.matrix data type to np.array like this:
A = np.array(M2)
print ("A = \n%s\n" % A)

# You can transpose them too:
print ("A.T = \n%s\n" % A.T)
