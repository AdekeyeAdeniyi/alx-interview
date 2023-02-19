# 0. Rotate 2D Matrix
### Given an n x n 2D matrix, rotate it 90 degrees clockwise.
---

- Prototype: def rotate_2d_matrix(matrix):
- Do not return anything. The matrix must be edited in-place.
- You can assume the matrix will have 2 dimensions and will not be empty.

## Pseudocode  Code
```sql
    1. Initialize the input matrix.
    2. For each index i in the range from 0 to the length of the matrix:
    3. Initialize an empty array arr of length equal to the number of rows in the matrix.
    4. For each index j in the range from the length of the matrix minus 1 to 0 (inclusive) in reverse order:
        5. Set the j-th element of arr to the i-th element of the j-th row of the matrix.
    6. Reverse the order of the elements in arr.
    7. Print arr.
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