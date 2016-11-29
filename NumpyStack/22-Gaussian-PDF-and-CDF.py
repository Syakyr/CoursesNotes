from scipy.stats import norm
import numpy as np
import time

def TimeElapsed(ID, function):
    start = time.perf_counter()
    print("Method %s:" % ID)
    calc = function
    elapsed = time.perf_counter() - start
    print("Answer is %s, elapsed in %s seconds\n" % (calc, elapsed))
    return elapsed


# loc = mean
# scale = standard deviation

print(norm.pdf(0, loc=5, scale=10))

r = np.random.randn(10)

elapsed1 = TimeElapsed(1, norm.pdf(r))

# Using LogPDF is much faster for calculation
# since you're using summation instead of
# product, which is a faster computation
# See 22.1-Log-PDF.png
elapsed2 = TimeElapsed(2, norm.logpdf(r))

# Speed Factor
factor21 = elapsed1 / elapsed2
print("Method 2 is %s faster than Method 1" % factor21)

# Also, see norm.cdf and norm.logcdf.