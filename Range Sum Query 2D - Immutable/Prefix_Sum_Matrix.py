'''
304. Range Sum Query 2D - Immutable

Given a 2D matrix, handle multiple queries of the following type:

    sumRegion(row1, col1, row2, col2)

Return the sum of all elements inside the rectangle defined by its upper-left
corner (row1, col1) and lower-right corner (row2, col2), inclusive.

Implement the NumMatrix class:

    - NumMatrix(matrix) Initializes the object with the integer matrix.
    - sumRegion(row1, col1, row2, col2) Returns the sum of the specified rectangle.

Example 1:
    Input:
        ["NumMatrix","sumRegion","sumRegion","sumRegion"]
        [[
          [
            [3,0,1,4,2],
            [5,6,3,2,1],
            [1,2,0,1,5],
            [4,1,0,1,7],
            [1,0,3,0,5]
          ]
        ],[2,1,4,3],[1,1,2,2],[1,2,2,4]]

    Output:
        [null,8,11,12]

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10^5 <= matrix[i][j] <= 10^5
    0 <= row1 <= row2 < m
    0 <= col1 <= col2 < n
    At most 10^4 calls will be made to sumRegion().
'''

# 2D Prefix Sum

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix = [[0]]
            return

        rows = len(matrix)
        cols = len(matrix[0])

        # Extra row and column simplify calculations.
        self.prefix = [
            [0] * (cols + 1)
            for _ in range(rows + 1)
        ]

        for row in range(rows):
            for col in range(cols):
                self.prefix[row + 1][col + 1] = (
                    matrix[row][col]
                    + self.prefix[row][col + 1]
                    + self.prefix[row + 1][col]
                    - self.prefix[row][col]
                )

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        return (
            self.prefix[row2 + 1][col2 + 1]
            - self.prefix[row1][col2 + 1]
            - self.prefix[row2 + 1][col1]
            + self.prefix[row1][col1]
        )


# Example usage

matrix = [
    [3,0,1,4,2],
    [5,6,3,2,1],
    [1,2,0,1,5],
    [4,1,0,1,7],
    [1,0,3,0,5]
]

numMatrix = NumMatrix(matrix)

# Example 1
print(numMatrix.sumRegion(2, 1, 4, 3))
# Output: 8

# Example 2
print(numMatrix.sumRegion(1, 1, 2, 2))
# Output: 11

# Example 3
print(numMatrix.sumRegion(1, 2, 2, 4))
# Output: 12

# Example 4
print(numMatrix.sumRegion(0, 0, 4, 4))
# Output: 58

# Example 5
matrix2 = [
    [1,2],
    [3,4]
]

numMatrix2 = NumMatrix(matrix2)

print(numMatrix2.sumRegion(0, 0, 1, 1))
# Output: 10

print(numMatrix2.sumRegion(0, 1, 1, 1))
# Output: 6
