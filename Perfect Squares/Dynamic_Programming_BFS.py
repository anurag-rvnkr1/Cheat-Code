'''
279. Perfect Squares

Given an integer n, return the least number of perfect square numbers
that sum to n.

A perfect square is an integer that is the square of an integer.

Example 1:
    Input: n = 12
    Output: 3

Explanation:
    12 = 4 + 4 + 4

Example 2:
    Input: n = 13
    Output: 2

Explanation:
    13 = 4 + 9

Constraints:
    1 <= n <= 10^4
'''

# Dynamic Programming

from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        # Generate all perfect squares <= n.
        perfect_squares = []

        for i in range(1, isqrt(n) + 1):
            perfect_squares.append(i * i)

        # dp[i] = minimum perfect squares required to make i.
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for value in range(1, n + 1):
            for square in perfect_squares:
                if square > value:
                    break

                dp[value] = min(dp[value], dp[value - square] + 1)

        return dp[n]


# Example usage
solution = Solution()

# Example 1
n1 = 12
print(solution.numSquares(n1))
# Output: 3

# Example 2
n2 = 13
print(solution.numSquares(n2))
# Output: 2

# Example 3
n3 = 1
print(solution.numSquares(n3))
# Output: 1

# Example 4
n4 = 43
print(solution.numSquares(n4))
# Output: 3

# Example 5
n5 = 100
print(solution.numSquares(n5))
# Output: 1
