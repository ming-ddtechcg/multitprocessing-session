from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()
print("Process rank: %d" % rank)

if rank == 0:
    data = {1: 2}
    communicator.send(data, dest=1)
elif rank == 1:
    received = communicator.recv(source=0)
    print("On rank %d, recieved data %s" % (rank, received))