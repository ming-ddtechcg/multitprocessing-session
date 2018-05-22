from multiprocessing import Pool, Process
import time


def do_work(number):
    print("My number: %d" % number)
    time.sleep(0.01)
    return number + 2

pool = Pool(8)

results = pool.map_async(do_work, range(1000))

while not results.ready():
    time.sleep(1)

print(results)
