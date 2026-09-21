'''
308. Range Sum Query 2D - Mutable

Given a 2D matrix, handle multiple queries of the following types:

    1. update(row, col, val)
       Update matrix[row][col] to val.

    2. sumRegion(row1, col1, row2, col2)
       Return the sum of all elements inside the rectangle defined by its
       upper-left corner (row1, col1) and lower-right corner (row2, col2).

Implement the NumMatrix class.

Example 1:
    Input:
        ["NumMatrix","sumRegion","update","sumRegion"]

        [[
          [
            [3,0,1,4,2],
            [5,6,3,2,1],
            [1,2,0,1,5],
            [4,1,0,1,7],
            [1,0,3,0,5]
          ]
        ],
        [2,1,4,3],
        [3,2,2],
        [2,1,4,3]]

    Output:
        [null,8,null,10]

Explanation:
    sumRegion(2,1,4,3) = 8
    update(3,2,2)
    sumRegion(2,1,4,3) = 10

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    -10^5 <= matrix[i][j] <= 10^5
    At most 10^4 calls will be made to update() and sumRegion().
'''

# 2D Binary Indexed Tree (Fenwick Tree)

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.rows = 0
            self.cols = 0
            return

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.matrix = [
            [0] * self.cols
            for _ in range(self.rows)
        ]

        # 1-based Fenwick Tree.
        self.bit = [
            [0] * (self.cols + 1)
            for _ in range(self.rows + 1)
        ]

        # Build Fenwick Tree.
        for row in range(self.rows):
            for col in range(self.cols):
                self.update(row, col, matrix[row][col])

    def _add(self, row: int, col: int, delta: int):
        i = row + 1

        while i <= self.rows:
            j = col + 1

            while j <= self.cols:
                self.bit[i][j] += delta
                j += j & -j

            i += i & -i

    def update(self, row: int, col: int, val: int):
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val

        self._add(row, col, delta)

    def _prefix_sum(self, row: int, col: int) -> int:
        total = 0
        i = row + 1

        while i > 0:
            j = col + 1

            while j > 0:
                total += self.bit[i][j]
                j -= j & -j

            i -= i & -i

        return total

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:

        return (
            self._prefix_sum(row2, col2)
            - self._prefix_sum(row1 - 1, col2)
            - self._prefix_sum(row2, col1 - 1)
            + self._prefix_sum(row1 - 1, col1 - 1)
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
numMatrix.update(3, 2, 2)

print(numMatrix.sumRegion(2, 1, 4, 3))
# Output: 10

# Example 3
print(numMatrix.sumRegion(1, 1, 2, 2))
# Output: 11

# Example 4
numMatrix.update(0, 0, 10)

print(numMatrix.sumRegion(0, 0, 0, 4))
# Output: 17

# Example 5
matrix2 = [
    [1,2],
    [3,4]
]

numMatrix2 = NumMatrix(matrix2)

print(numMatrix2.sumRegion(0, 0, 1, 1))
# Output: 10

numMatrix2.update(1, 1, 8)

print(numMatrix2.sumRegion(0, 0, 1, 1))
# Output: 14
