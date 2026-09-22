'''
329. Longest Increasing Path in a Matrix

Given an m x n integer matrix, return the length of the longest
strictly increasing path in the matrix.

You may move in four directions:
    Up, Down, Left, Right

You may NOT move diagonally or outside the grid.

Example 1:
    Input:
        matrix = [
            [9,9,4],
            [6,6,8],
            [2,1,1]
        ]

    Output:
        4

Explanation:
    Longest increasing path:
        1 → 2 → 6 → 9

Example 2:
    Input:
        matrix = [
            [3,4,5],
            [3,2,6],
            [2,2,1]
        ]

    Output:
        4

Explanation:
    Longest increasing path:
        3 → 4 → 5 → 6

Example 3:
    Input:
        matrix = [[1]]

    Output:
        1

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m,n <= 200
    0 <= matrix[i][j] <= 2^31 - 1
'''

# DFS + Memoization (Topological DP)

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        memo = [[0] * cols for _ in range(rows)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(row: int, col: int) -> int:

            # Already computed.
            if memo[row][col]:
                return memo[row][col]

            longest = 1

            for dr, dc in directions:

                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows and
                    0 <= new_col < cols and
                    matrix[new_row][new_col] > matrix[row][col]
                ):
                    longest = max(
                        longest,
                        1 + dfs(new_row, new_col)
                    )

            memo[row][col] = longest

            return longest

        answer = 0

        for row in range(rows):
            for col in range(cols):
                answer = max(answer, dfs(row, col))

        return answer


# Example usage
solution = Solution()

# Example 1
matrix1 = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]

print(solution.longestIncreasingPath(matrix1))
# Output: 4

# Example 2
matrix2 = [
    [3,4,5],
    [3,2,6],
    [2,2,1]
]

print(solution.longestIncreasingPath(matrix2))
# Output: 4

# Example 3
matrix3 = [[1]]

print(solution.longestIncreasingPath(matrix3))
# Output: 1

# Example 4
matrix4 = [
    [7,8,9],
    [9,7,6],
    [7,2,3]
]

print(solution.longestIncreasingPath(matrix4))
# Output: 6

# Example 5
matrix5 = [
    [1,2],
    [3,4]
]

print(solution.longestIncreasingPath(matrix5))
# Output: 3
