'''
63. Unique Paths II

You are given an m x n integer array obstacleGrid. There is a robot initially located at the top-left corner (i.e., obstacleGrid[0][0]). The robot tries to move to the bottom-right corner (i.e., obstacleGrid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in obstacleGrid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
    Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    Output: 2
    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

Example 2:
    Input: obstacleGrid = [[0,1],[0,0]]
    Output: 1

Constraints:
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1
'''

# Dynamic Programming (2D DP with Obstacles)
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * n for _ in range(m)]

        # Starting cell is blocked
        if obstacleGrid[0][0] == 1:
            return 0

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):

                # Skip the starting cell
                if i == 0 and j == 0:
                    continue

                # Obstacle → no paths
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                else:
                    # Paths from above
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]

                    # Paths from left
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]


# Example usage
solution = Solution()

print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # Output: 2
print(solution.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # Output: 1
print(solution.uniquePathsWithObstacles([[1]]))  # Output: 0
print(solution.uniquePathsWithObstacles([[0]]))  # Output: 1
