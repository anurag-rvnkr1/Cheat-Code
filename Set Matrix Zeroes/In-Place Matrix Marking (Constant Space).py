'''
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
    - A straightforward solution using O(mn) space is probably a bad idea.
    - A simple improvement uses O(m + n) space, but still not the best solution.
    - Could you devise a constant space solution?
'''

# In-Place Matrix Marking (Constant Space)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains 0
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column contains 0
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Finally handle first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Finally handle first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0


# Example usage
solution = Solution()

matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix2)
print(matrix2)  # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
