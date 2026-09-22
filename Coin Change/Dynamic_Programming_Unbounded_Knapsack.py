'''
322. Coin Change

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins needed to make up that amount.

If that amount cannot be made up by any combination of the coins,
return -1.

You have an infinite number of each kind of coin.

Example 1:
    Input:
        coins = [1,2,5]
        amount = 11

    Output:
        3

Explanation:
        11 = 5 + 5 + 1

Example 2:
    Input:
        coins = [2]
        amount = 3

    Output:
        -1

Example 3:
    Input:
        coins = [1]
        amount = 0

    Output:
        0

Constraints:
    1 <= coins.length <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4
'''

# Dynamic Programming (Unbounded Knapsack)

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] = minimum coins needed to make amount i
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        # Build DP table from smaller amounts to larger amounts.
        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        return dp[amount] if dp[amount] != float("inf") else -1


# Example usage
solution = Solution()

# Example 1
coins1 = [1, 2, 5]
amount1 = 11
print(solution.coinChange(coins1, amount1))
# Output: 3

# Example 2
coins2 = [2]
amount2 = 3
print(solution.coinChange(coins2, amount2))
# Output: -1

# Example 3
coins3 = [1]
amount3 = 0
print(solution.coinChange(coins3, amount3))
# Output: 0

# Example 4
coins4 = [2, 5, 10, 1]
amount4 = 27
print(solution.coinChange(coins4, amount4))
# Output: 4
# 10 + 10 + 5 + 2

# Example 5
coins5 = [2, 4, 6]
amount5 = 8
print(solution.coinChange(coins5, amount5))
# Output: 2
# 4 + 4

# Example 6
coins6 = [186, 419, 83, 408]
amount6 = 6249
print(solution.coinChange(coins6, amount6))
# Output: 20
