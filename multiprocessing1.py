

from multiprocessing import Process
import os


def add_number(number):
    new_number = number + 10
    print("I am on process %d. My result is %d" % (os.getpid(), new_number))


process = Process(target=add_number, args=(10,))
process2 = Process(target=add_number, args=(20,))
process.start()
process2.start()

process.join()

print("Finished")
process2.join()
