from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Input matrices
if rank == 0:
    A = np.array([[1, 2], [3, 4]], dtype=int)
    B = np.array([[5, 6], [7, 8]], dtype=int)
    comm.bcast(A,root=0)
    comm.bcast(B,root=0)
else:
    A = comm.bcast(None,root=0)
    B = comm.bcast(None,root=0)

# Divide the input matrices across the processes
local_size = A.shape[0] // size
local_A = A[rank]
local_B = B[rank]

comm.barrier()

# Compute the local sum of the matrices
local_C = local_A + local_B
# Gather the local results into the final result

comm.barrier()
C = None
if rank == 0:
    C = np.zeros((A.shape[0], A.shape[1]), dtype=int)
comm.Gather(local_C, C, root=0)

comm.barrier()
# Print the result
if rank == 0:
    print("A:\n", A)
    print("B:\n", B)
    print("C:\n", C)
