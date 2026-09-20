'''
134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the
ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station.

You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if
you can travel around the circuit once in the clockwise direction, otherwise return -1.

If there exists a solution, it is guaranteed to be unique.

Example 1:
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3

Explanation:
    Start at station 3 and travel around the circuit once.

Example 2:
    Input: gas = [2,3,4], cost = [3,4,3]
    Output: -1

Constraints:
    n == gas.length == cost.length
    1 <= n <= 10^5
    0 <= gas[i], cost[i] <= 10^4
'''

# Greedy

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            difference = gas[i] - cost[i]

            total_gas += difference
            current_gas += difference

            # Cannot reach next station, choose next station as new start.
            if current_gas < 0:
                start = i + 1
                current_gas = 0

        return start if total_gas >= 0 else -1


# Example usage
solution = Solution()

# Example 1
gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]

print(solution.canCompleteCircuit(gas1, cost1))  # Output: 3

# Example 2
gas2 = [2, 3, 4]
cost2 = [3, 4, 3]

print(solution.canCompleteCircuit(gas2, cost2))  # Output: -1

# Example 3
gas3 = [5, 1, 2, 3, 4]
cost3 = [4, 4, 1, 5, 1]

print(solution.canCompleteCircuit(gas3, cost3))  # Output: 4
