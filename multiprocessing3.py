from multiprocessing import Process, Pool
import time

def compute(n):
    time.sleep(0.01)
    return pow(n, 2)

pool = Pool(4)
results = pool.map_async(compute, range(1000))

while not results.ready():
    time.sleep(1)

print(results.get())