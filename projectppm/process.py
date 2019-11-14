import numpy as np
import sys

M, S = int(sys.argv[1]), int(sys.argv[2])

lines = [L.strip() for L in sys.stdin.readlines()]
mat = np.array([float(L) for L in lines[1].split(' ')]).reshape((M, S))

assert np.allclose(0, mat[mat < 0])
mat[mat < 0] = 0
print(np.any(np.isnan(mat)))
print(np.sum(mat, axis=0))
