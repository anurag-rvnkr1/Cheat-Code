'''
265. Paint House II

There are a row of n houses, where each house can be painted one of k colors.

The cost of painting each house with a certain color is represented by
costs[i][j], where costs[i][j] is the cost of painting house i with color j.

You cannot paint two adjacent houses with the same color.

Return the minimum cost to paint all houses.

Example 1:
    Input:
        costs = [
            [1,5,3],
            [2,9,4]
        ]

    Output: 5

Explanation:
    Paint House 0 with Color 0 (Cost = 1)
    Paint House 1 with Color 2 (Cost = 4)

    Total Cost = 1 + 4 = 5

Example 2:
    Input:
        costs = [[1,3]]

    Output: 1

Constraints:
    n == costs.length
    k == costs[i].length
    1 <= n <= 100
    2 <= k <= 20
    1 <= costs[i][j] <= 20

Follow-up:
    Can you solve it in O(n * k) time?
'''

# Dynamic Programming

from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])

        previous_min = 0
        previous_second_min = 0
        previous_color = -1

        for house in range(n):
            current_min = float("inf")
            current_second_min = float("inf")
            current_color = -1

            for color in range(k):

                if color == previous_color:
                    costs[house][color] += previous_second_min
                else:
                    costs[house][color] += previous_min

                if costs[house][color] < current_min:
                    current_second_min = current_min
                    current_min = costs[house][color]
                    current_color = color

                elif costs[house][color] < current_second_min:
                    current_second_min = costs[house][color]

            previous_min = current_min
            previous_second_min = current_second_min
            previous_color = current_color

        return previous_min


# Example usage
solution = Solution()

# Example 1
costs1 = [
    [1, 5, 3],
    [2, 9, 4]
]

print(solution.minCostII(costs1))
# Output: 5

# Example 2
costs2 = [
    [1, 3]
]

print(solution.minCostII(costs2))
# Output: 1

# Example 3
costs3 = [
    [8, 16, 12],
    [10, 5, 18],
    [7, 14, 3],
    [9, 2, 6]
]

print(solution.minCostII(costs3))
# Output: 18

# Example 4
costs4 = [
    [3, 5, 7, 2],
    [8, 1, 4, 9],
    [6, 3, 2, 5]
]

print(solution.minCostII(costs4))
# Output: 5
