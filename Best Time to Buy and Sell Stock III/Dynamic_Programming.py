'''
123. Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note:
You may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6

Explanation:
    Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 3.
    Total profit = 6.

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0

Constraints:
    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
'''

# Dynamic Programming (State Machine)

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float("-inf")
        sell1 = 0
        buy2 = float("-inf")
        sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2


# Example usage
solution = Solution()

# Example 1
prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
print(solution.maxProfit(prices1))  # Output: 6

# Example 2
prices2 = [1, 2, 3, 4, 5]
print(solution.maxProfit(prices2))  # Output: 4

# Example 3
prices3 = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices3))  # Output: 0

# Example 4
prices4 = [1]
print(solution.maxProfit(prices4))  # Output: 0
