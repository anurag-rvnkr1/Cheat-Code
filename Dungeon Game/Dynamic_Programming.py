'''
174. Dungeon Game

The demons had captured the princess and imprisoned her in the bottom-right corner
of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid.

The knight starts in the top-left room and must reach the princess in the
bottom-right room.

Each room contains an integer:
    - Negative value: The knight loses health.
    - Positive value: The knight gains health.
    - Zero: No effect on health.

The knight's health must never drop to 0 or below at any point.

Return the knight's minimum initial health required to rescue the princess.

Example 1:
    Input: dungeon = [
        [-2,-3,3],
        [-5,-10,1],
        [10,30,-5]
    ]
    Output: 7

Example 2:
    Input: dungeon = [[0]]
    Output: 1

Constraints:
    m == dungeon.length
    n == dungeon[i].length
    1 <= m, n <= 200
    -1000 <= dungeon[i][j] <= 1000
'''

# Dynamic Programming (Bottom-Up)

from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])

        # Extra row and column initialized with infinity.
        dp = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]

        # Base case.
        dp[rows][cols - 1] = 1
        dp[rows - 1][cols] = 1

        # Fill DP table from bottom-right to top-left.
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                health_needed = min(dp[r + 1][c], dp[r][c + 1]) - dungeon[r][c]
                dp[r][c] = max(1, health_needed)

        return dp[0][0]


# Example usage
solution = Solution()

# Example 1
dungeon1 = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]

print(solution.calculateMinimumHP(dungeon1))  # Output: 7

# Example 2
dungeon2 = [[0]]

print(solution.calculateMinimumHP(dungeon2))  # Output: 1

# Example 3
dungeon3 = [[100]]

print(solution.calculateMinimumHP(dungeon3))  # Output: 1

# Example 4
dungeon4 = [[-3, 5]]

print(solution.calculateMinimumHP(dungeon4))  # Output: 4
