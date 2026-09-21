'''
256. Paint House

There are a row of n houses, where each house can be painted one of three colors:
red, blue, or green.

The cost of painting each house with a certain color is represented by
costs[i][j], where:
    - costs[i][0] = cost of painting house i red.
    - costs[i][1] = cost of painting house i blue.
    - costs[i][2] = cost of painting house i green.

No two adjacent houses can have the same color.

Return the minimum cost to paint all houses.

Example 1:
    Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
    Output: 10

Explanation:
    Paint house 0 Blue (2)
    Paint house 1 Green (5)
    Paint house 2 Blue (3)
    Total cost = 2 + 5 + 3 = 10

Example 2:
    Input: costs = [[7,6,2]]
    Output: 2

Constraints:
    costs.length == n
    1 <= n <= 100
    costs[i].length == 3
    1 <= costs[i][j] <= 20
'''

# Dynamic Programming

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        # Process each house starting from the second one.
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        # Minimum cost among the three colors for the last house.
        return min(costs[-1])


# Example usage
solution = Solution()

# Example 1
costs1 = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]

print(solution.minCost(costs1))
# Output: 10

# Example 2
costs2 = [[7, 6, 2]]

print(solution.minCost(costs2))
# Output: 2

# Example 3
costs3 = [
    [1, 5, 3],
    [2, 9, 4]
]

print(solution.minCost(costs3))
# Output: 5

# Example 4
costs4 = [
    [8, 16, 12],
    [10, 5, 18],
    [7, 14, 3],
    [9, 2, 6]
]

print(solution.minCost(costs4))
# Output: 22
