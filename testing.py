from multiprocessing import Process, Queue


def compute(n):
    print("%d, %d" % (n, pow(n, 2)))

process = Process(target=compute, args=(10,))
process2 = Process(target=compute, args=(11,))

process.start()
process2.start()

print("Finished")
process2.join()
process.join()

