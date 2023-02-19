#!/usr/bin/python3
"""
Transpose and reverse the columns of a matrix.

Given a matrix, this function transposes the columns
and stores each transposed column in a new row
of the resulting matrix. It then reverses the
order of the elements in each row and prints the
resulting matrix to the console.

Args:
    matrix: A list of lists representing the input matrix.

Returns:
    None.
"""


def rotate_2d_matrix(matrix):
    if not matrix or len(matrix) <= 1:
        return
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            matrix[i][j], matrix[n - 1 - j][i], \
                matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = \
                matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], \
                matrix[j][n - 1 - i], matrix[i][j]
