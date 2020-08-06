from typing import List


class Matrix(object):
    def __init__(self, matrix: List[List]):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(item) for item in row])
                          for row in self.matrix])

    def __add__(self, other):
        sum_matrix = []
        for ind_row, row in enumerate(self.matrix):
            row_sum_matrix = []
            for ind_el, el in enumerate(row):
                row_sum_matrix.append(el + other.matrix[ind_row][ind_el])
            sum_matrix.append(row_sum_matrix)
        return Matrix(sum_matrix)


matrix1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(matrix1)

matrix2 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(matrix2)

matrix3 = matrix1 + matrix2
print(matrix3)
