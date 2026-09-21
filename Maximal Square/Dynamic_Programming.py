'''
221. Maximal Square

Given an m x n binary matrix filled with '0's and '1's, find the largest square
containing only '1's and return its area.

Example 1:
    Input:
        matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
    Output: 4

Explanation:
    The largest square containing only '1's has side length 2.
    Area = 2 × 2 = 4.

Example 2:
    Input:
        matrix = [
            ["0","1"],
            ["1","0"]
        ]
    Output: 1

Example 3:
    Input:
        matrix = [["0"]]
    Output: 0

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is '0' or '1'.
'''

# Dynamic Programming

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        # Extra row and column simplify boundary conditions.
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = 1 + min(
                        dp[r - 1][c],      # Top
                        dp[r][c - 1],      # Left
                        dp[r - 1][c - 1]   # Top-left
                    )

                    max_side = max(max_side, dp[r][c])

        return max_side * max_side


# Example usage
solution = Solution()

# Example 1
matrix1 = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

print(solution.maximalSquare(matrix1))  # Output: 4

# Example 2
matrix2 = [
    ["0","1"],
    ["1","0"]
]

print(solution.maximalSquare(matrix2))  # Output: 1

# Example 3
matrix3 = [["0"]]

print(solution.maximalSquare(matrix3))  # Output: 0

# Example 4
matrix4 = [
    ["1","1","1"],
    ["1","1","1"],
    ["1","1","1"]
]

print(solution.maximalSquare(matrix4))  # Output: 9
