import numpy as np
import time

a = np.random.rand(100)
b = np.random.rand(100)
T = 100000

def slow_dot_product(a, b):
    result = 0
    for e, f in zip(a,b): result += e*f
    return result

t0 = time.perf_counter()
for t in range(T):
    slow_dot_product(a,b)
dt1 = time.perf_counter() - t0

t0 = time.perf_counter()
for t in range(T):
    a.dot(b)
dt2 = time.perf_counter() - t0

print ("dt1 / dt2 = %s" % (dt1/dt2))