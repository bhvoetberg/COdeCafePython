from copy import copy
from copy import deepcopy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_copy = deepcopy(matrix)

print(id(matrix) == id(matrix_copy))

print(id(matrix[0]) == id(matrix_copy[0]))

print(id(matrix[1]) == id(matrix_copy[1]))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_copy = copy(matrix)
matrix_copy[0][0] = 100
matrix_copy[0][1] = 200
matrix_copy[0][2] = 300
print(matrix_copy)
print(matrix)


