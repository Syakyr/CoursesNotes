import numpy as np
import time
X = []

start = time.perf_counter()
for line in open("data_2d.csv"):
    row = line.split(',')
    sample = []
    for i in row:
        n = float(i)
        sample.append(n)
    X.append(sample)
X = np.array(X)
print(X)
elapsed = time.perf_counter() - start
print("Elapsed time: %s seconds" % elapsed)