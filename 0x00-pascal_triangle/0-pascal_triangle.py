#!/usr/bin/python3
"""
    Return List of intger representing a Pascal's Triangle.
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    result = []
    for i in range(n + 1):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(row)
    return result
