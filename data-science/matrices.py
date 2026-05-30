import numpy as np

matrix1 = np.random.randint(0,17,(4,4))
matrix1 = np.random.permutation(matrix1)

matrix2 = np.random.randint(0,17,(4,4))
matrix2 = np.random.permutation(matrix2)

print(matrix1)
print(matrix2)

print(matrix1 + matrix2)
print(np.matmul(matrix1,matrix2))