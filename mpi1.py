# mpirun -np 4 python3 mpi1.py

from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

print("Size: %d, rank: %d" % (size, rank))

if rank == 0:
    data = {1: "Test"}
    comm.Send(np.zeros(1000, dtype=np.int8) + 1, dest=1)
elif rank == 1:
    rec_data = np.zeros(1000, dtype=np.int16)
    comm.Recv(rec_data, source=0)
    print("Received %s on process %d"  % (rec_data, rank))