from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from queue import Empty
import time
import numpy as np
import os

a = np.random.randint(0, 100, 100000)
B = np.arange(0, 1000000000)

def compute(n):
    B.sum()
    print(id(a))
    print(os.getpid())
    a.copy().sort()
    a[n] = 10
    return pow(n, 2)


n_workers = 4
pool = Pool(n_workers)
results = pool.map(compute, range(4))
print(a[0:4])
