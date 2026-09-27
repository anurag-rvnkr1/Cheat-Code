'''
518. Coin Change II

You are given an integer amount and an array of coin denominations coins.

Return the number of combinations that make up the amount.

You have an infinite number of each type of coin.

Example 1:
    Input:
        amount = 5
        coins = [1,2,5]

    Output:
        4

Explanation:
        The four combinations are:
        5
        2 + 2 + 1
        2 + 1 + 1 + 1
        1 + 1 + 1 + 1 + 1

Example 2:
    Input:
        amount = 3
        coins = [2]

    Output:
        0

Example 3:
    Input:
        amount = 10
        coins = [10]

    Output:
        1

Constraints:
    0 <= amount <= 5000
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All coin values are unique.
'''

# Dynamic Programming (Unbounded Knapsack)

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Process each coin once to count combinations.
        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] += dp[current_amount - coin]

        return dp[amount]


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.change(5, [1,2,5]))
# Output: 4

# Example 2
print(solution.change(3, [2]))
# Output: 0

# Example 3
print(solution.change(10, [10]))
# Output: 1

# Example 4
print(solution.change(0, [1,2,5]))
# Output: 1

# Example 5
print(solution.change(4, [1,2,3]))
# Output: 4

# Example 6
print(solution.change(7, [1,3,4,5]))
# Output: 6
