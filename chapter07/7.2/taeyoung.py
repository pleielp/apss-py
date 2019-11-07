import numpy as np
from numpy.linalg import matrix_power as matrix_power_np


def matrix_power_dq(A, m):
    if m == 0:
        return np.identity(len(A), dtype=int)
    elif m % 2 == 1:
        return np.matmul(pow(A, m - 1), A)
        
    half = pow(A, m // 2)
    return np.matmul(half, half)


test_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix_power_dq(test_array, 2))
print(matrix_power_np(test_array, 2))