'''
375. Guess Number Higher or Lower II

We are playing the Guess Game.

This time, you must pay the amount of every wrong guess.

Given n, return the minimum amount of money required to guarantee a win.

Example 1:
    Input:
        n = 10

    Output:
        16

Example 2:
    Input:
        n = 1

    Output:
        0

Example 3:
    Input:
        n = 2

    Output:
        1

Constraints:
    1 <= n <= 200
'''

# Dynamic Programming + Minimax (Interval DP)

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # Length of interval.
        for length in range(2, n + 1):

            for left in range(1, n - length + 2):
                right = left + length - 1

                dp[left][right] = float("inf")

                for guess in range(left, right + 1):
                    cost = guess + max(
                        dp[left][guess - 1],
                        dp[guess + 1][right]
                    )

                    dp[left][right] = min(dp[left][right], cost)

        return dp[1][n]


# Example usage
solution = Solution()

# Example 1
print(solution.getMoneyAmount(10))
# Output: 16

# Example 2
print(solution.getMoneyAmount(1))
# Output: 0

# Example 3
print(solution.getMoneyAmount(2))
# Output: 1

# Example 4
print(solution.getMoneyAmount(5))
# Output: 6

# Example 5
print(solution.getMoneyAmount(7))
# Output: 10

# Example 6
print(solution.getMoneyAmount(20))
# Output: 49
