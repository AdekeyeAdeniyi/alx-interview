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
    newMatrix = []
    if len(matrix) <= 1 or not matrix:
        return matrix
    for i in range(len(matrix)):
        arr = [0] * len(matrix)
        for j in range(len(matrix) - 1, -1, -1):
            arr[j] = matrix[j][i]
        newMatrix.append(list(reversed(arr)))
    return newMatrix
