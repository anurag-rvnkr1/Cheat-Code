'''
120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i in the current row, you may move to
either index i or index i + 1 on the next row.

Example 1:
    Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    Output: 11

Explanation:
    The triangle looks like:
           2
          3 4
         6 5 7
        4 1 8 3

    The minimum path sum from top to bottom is:
    2 + 3 + 5 + 1 = 11.

Example 2:
    Input: triangle = [[-10]]
    Output: -10

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4
'''

# Bottom-Up Dynamic Programming

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Copy the last row as the initial DP array.
        dp = triangle[-1][:]

        # Process rows from bottom to top.
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]


# Example usage
solution = Solution()

# Example 1
triangle1 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print(solution.minimumTotal(triangle1))  # Output: 11

# Example 2
triangle2 = [[-10]]

print(solution.minimumTotal(triangle2))  # Output: -10

# Example 3
triangle3 = [
    [1],
    [2, 3],
    [3, 6, 7],
    [8, 9, 6, 10]
]

print(solution.minimumTotal(triangle3))  # Output: 12
