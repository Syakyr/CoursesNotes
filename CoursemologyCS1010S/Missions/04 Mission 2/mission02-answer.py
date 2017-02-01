#
# CS1010S --- Programming Methodology
#
# Mission 2
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from runes import *


###########
# Task 1a #
###########

def fractal(painter, n, count=1):
    if (count == n): return stackn(2**(count-1), painter)
    else: return beside(stackn(2**(count-1), painter),fractal(painter, n, count+1))

# Test
# show(fractal(make_cross(rcross_bb), 3))
# show(fractal(make_cross(rcross_bb), 7))
# Write your additional test cases here

###########
# Task 1b #
###########

def fractal_iter(painter, n):
    result = stackn(2**(n-1), painter)
    for i in range(n-2, -1, -1):
        result = beside(stackn(2**i, painter), result)
    return result

# Test
# show(fractal_iter(make_cross(rcross_bb), 3))
# show(fractal_iter(make_cross(rcross_bb), 7))
# Write your additional test cases here


###########
# Task 1c #
###########

def dual_fractal(p1, p2, n, count=1):
    if (count % 2): painter = p1
    else: painter = p2
    if (count == n): return stackn(2**(count-1), painter)
    else: return beside(stackn(2**(count-1), painter),dual_fractal(p1, p2, n, count+1))

# Test
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

###########
# Task 1d #
###########

def dual_fractal_iter(p1, p2, n):
    if (n % 2): painter = p1
    else: painter = p2
    
    result = stackn(2**(n-1), painter)
    for i in range(n-2, -1, -1):
        if (i % 2): painter = p2
        else: painter = p1
        result = beside(stackn(2**i, painter), result)
    return result

# Test
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 3))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 4))
# show(dual_fractal_iter(make_cross(rcross_bb), make_cross(nova_bb), 7))
# Write your additional test cases here

# Note that when n is even, the first (biggest) rune should still be rune1

##########
# Task 2 #
##########

def steps(p1, p2, p3, p4):
    bl = blank_bb
    p1 = beside(bl,stack(p1,bl))
    p2 = beside(bl,stack(bl,p2))
    p3 = beside(stack(bl,p3),bl)
    p4 = beside(stack(p4,bl),bl)
    return overlay(overlay(p4, p3),overlay(p2, p1))

# Test
#show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))
