'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a target value in an m x n integer matrix.

This matrix has the following properties:

    - Integers in each row are sorted in ascending from left to right.
    - Integers in each column are sorted in ascending from top to bottom.

Return True if target is in matrix, otherwise return False.

Example 1:
    Input:
        matrix = [
            [1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]
        ]
        target = 5

    Output: True

Example 2:
    Input:
        matrix = [
            [1,4,7,11,15],
            [2,5,8,12,19],
            [3,6,9,16,22],
            [10,13,14,17,24],
            [18,21,23,26,30]
        ]
        target = 20

    Output: False

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    -10^9 <= matrix[i][j] <= 10^9
    All rows are sorted in ascending order.
    All columns are sorted in ascending order.
'''

# Matrix + Binary Search (Top-Right Search)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Start from the top-right corner.
        row = 0
        col = cols - 1

        while row < rows and col >= 0:

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                col -= 1

            else:
                row += 1

        return False


# Example usage
solution = Solution()

# Example 1
matrix1 = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(solution.searchMatrix(matrix1, 5))   # Output: True

# Example 2
print(solution.searchMatrix(matrix1, 20))  # Output: False

# Example 3
matrix2 = [[-5]]

print(solution.searchMatrix(matrix2, -5))  # Output: True

# Example 4
matrix3 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]

print(solution.searchMatrix(matrix3, 8))   # Output: True
