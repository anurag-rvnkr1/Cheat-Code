'''
188. Best Time to Buy and Sell Stock IV

You are given an integer k and an integer array prices where prices[i] is the
price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note:
    You may not engage in multiple transactions simultaneously
    (i.e., you must sell the stock before buying again).

Example 1:
    Input: k = 2, prices = [2,4,1]
    Output: 2

Explanation:
    Buy on day 1 (price = 2) and sell on day 2 (price = 4).
    Profit = 2.

Example 2:
    Input: k = 2, prices = [3,2,6,5,0,3]
    Output: 7

Explanation:
    Buy on day 2 (price = 2) and sell on day 3 (price = 6).
    Profit = 4.
    Buy on day 5 (price = 0) and sell on day 6 (price = 3).
    Profit = 3.
    Total profit = 7.

Constraints:
    1 <= k <= 100
    1 <= prices.length <= 1000
    0 <= prices[i] <= 1000
'''

# Dynamic Programming

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        n = len(prices)

        # If k is large enough, treat it as unlimited transactions.
        if k >= n // 2:
            profit = 0

            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        # buy[i]  = Maximum profit after buying the i-th stock.
        # sell[i] = Maximum profit after selling the i-th stock.
        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for transaction in range(1, k + 1):
                buy[transaction] = max(
                    buy[transaction],
                    sell[transaction - 1] - price
                )

                sell[transaction] = max(
                    sell[transaction],
                    buy[transaction] + price
                )

        return sell[k]


# Example usage
solution = Solution()

# Example 1
k1 = 2
prices1 = [2, 4, 1]
print(solution.maxProfit(k1, prices1))  # Output: 2

# Example 2
k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
print(solution.maxProfit(k2, prices2))  # Output: 7

# Example 3
k3 = 1
prices3 = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(k3, prices3))  # Output: 5

# Example 4
k4 = 3
prices4 = [1, 2, 3, 4, 5]
print(solution.maxProfit(k4, prices4))  # Output: 4
