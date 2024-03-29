from mpi4py import MPI
import numpy as np

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
print("Rank is ",rank)
print("Size is ",size)
print(comm.Get_name())
# Define matrix sizes
m = 4  # rows of matrix A
n = 2 # columns of matrix A / rows of matrix B
p = 4 # columns of matrix B

# Create random matrices A and B on rank 0

if rank == 0:
    A = np.random.randint(low=1, high=10, size=(m, n))
    B = np.random.randint(low=1, high=10, size=(n, p))
    comm.bcast(A, root=0)
    comm.bcast(B, root=0)
else:
    A = comm.bcast(None, root=0)
    B = comm.bcast(None, root=0)

# Broadcast matrices A and B to all processes
# A = comm.bcast(A, root=0)
# B = comm.bcast(B, root=0)

comm.barrier()
# Compute local matrix multiplication
local_C = np.zeros((m//size, p))
for i in range(m//size):
    for j in range(p):
        for k in range(n):
            local_C[i, j] += A[i+rank*m//size, k] * B[k, j]
print(local_C)

comm.barrier()
# Gather local C matrices on rank 0
C = None
if rank == 0:
    C = np.zeros((m, p))

comm.barrier()
comm.Gather(local_C, C, root=0)

# Print result on rank 0
if rank == 0:
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C:")
    print(C)