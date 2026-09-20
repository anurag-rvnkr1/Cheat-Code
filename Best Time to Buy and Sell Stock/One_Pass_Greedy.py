'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5

Explanation:
    Buy on day 2 (price = 1) and sell on day 5 (price = 6).
    Profit = 6 - 1 = 5.

Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0

Explanation:
    No transaction is done because the prices keep decreasing.

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^4
'''

# One-Pass Greedy

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


# Example usage
solution = Solution()

# Example 1
prices1 = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices1))  # Output: 5

# Example 2
prices2 = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices2))  # Output: 0

# Example 3
prices3 = [2, 4, 1]
print(solution.maxProfit(prices3))  # Output: 2
