from multiprocessing import Queue, Process


def worker(queue):
    while True:
        number = queue.get()
        if number is None:
            break

        print("%d, %d" % (number, number**2))

queue = Queue()
for i in range(10000):
    queue.put(i)

for i in range(10):
    queue.put(None)
    p = Process(target=worker, args=(queue,))
    p.start()



