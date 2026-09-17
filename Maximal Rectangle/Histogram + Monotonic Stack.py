'''
85. Maximal Rectangle

Given a rows x cols binary matrix filled with '0's and '1's, find the largest rectangle containing only '1's and return its area.

Example 1:
    Input:
        matrix = [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
        ]
    Output: 6
    Explanation:
    The maximal rectangle contains only '1's and has an area of 6.

Example 2:
    Input: matrix = [["0"]]
    Output: 0

Example 3:
    Input: matrix = [["1"]]
    Output: 1

Constraints:
    rows == matrix.length
    cols == matrix[i].length
    1 <= rows, cols <= 200
    matrix[i][j] is '0' or '1'.
'''

# Histogram + Monotonic Stack
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:

            # Build histogram heights for the current row
            for j in range(cols):
                if row[j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Largest Rectangle in Histogram
            stack = []

            for i in range(cols + 1):
                height = heights[i] if i < cols else 0

                while stack and heights[stack[-1]] > height:
                    h = heights[stack.pop()]

                    left = stack[-1] if stack else -1
                    width = i - left - 1

                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area


# Example usage
solution = Solution()

matrix1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(solution.maximalRectangle(matrix1))  # Output: 6

matrix2 = [["0"]]
print(solution.maximalRectangle(matrix2))  # Output: 0

matrix3 = [["1"]]
print(solution.maximalRectangle(matrix3))  # Output: 1
