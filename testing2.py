from multiprocessing import Process, Queue

def worker(queue, out_queue):
    while True:
        number = queue.get()
        if number is None:
            break
        #print("%d, %d" % (number, pow(number, 4)))
        out_queue.put(pow(number, 4))

queue = Queue()
out_queue = Queue()

for i in range(100):
    queue.put(i)

n_workers = 4
processes = []
for i in range(n_workers):
    queue.put(None)
    p = Process(target=worker, args=(queue, out_queue))
    p.start()
    processes.append(p)

for process in processes:
    process.join()

