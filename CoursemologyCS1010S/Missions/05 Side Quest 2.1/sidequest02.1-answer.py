#
# CS1010S --- Programming Methodology
#
# Mission 2 - Side Quest 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *
import math

##########
# Task 1 #
##########

def tree(n, painter):
    result = scale(1/n, painter)
    for i in range(2, n+1):
        result = overlay_frac((i-1)/i,result, scale(i/n, painter))
    return result

# Test
#show(tree(4, circle_bb))


##########
# Task 2 #
##########

# use help(math) to see functions in math module
# e.g to find out value of sin(pi/2), call math.sin(math.pi/2)

def helix(painter, n):
    
    L = 1/2 - 1/n
    s = 2/n
    
    result = translate(L*cos(pi/2), L*sin(pi/2), scale(2/n, painter))
    for i in range(2, n+1):
        foo = translate(L*cos(pi/2 - 2*pi*(i-1)/n),L*sin(pi/2 - 2*pi*(i-1)/n),scale(2/n, painter))
        result = overlay_frac((i-1)/i,result, foo)
    return result

# Test
#show(helix(make_cross(rcross_bb), 9))
