# 0. Rotate 2D Matrix
### Given an n x n 2D matrix, rotate it 90 degrees clockwise.
---

- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

## Pseudocode  Code
```sql
    1. Define a function called "rotate_2d_matrix" that takes a matrix as input
    2. Check if the matrix is not empty or has only one row, and return it if so
    3. Find the length of the matrix and divide it by 2
    4. Loop from 0 to the length of the matrix divided by 2
    5. Loop from i to the length of the matrix minus i minus 1
    6. Swap the values in the matrix at the following locations:
    a. matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i]
    b. where n is the length of the matrix
    7. Return the modified matrix

```

```js
    """input"""
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    
    """output"""
    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]

```