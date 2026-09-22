'''
365. Water and Jug Problem

You are given two jugs with capacities jug1Capacity and jug2Capacity liters,
and an infinite supply of water.

Return True if it is possible to measure exactly targetCapacity liters.

Allowed operations:
    - Fill either jug completely.
    - Empty either jug completely.
    - Pour water from one jug into the other until one is empty or the other is full.

Example 1:
    Input:
        jug1Capacity = 3
        jug2Capacity = 5
        targetCapacity = 4

    Output:
        True

Example 2:
    Input:
        jug1Capacity = 2
        jug2Capacity = 6
        targetCapacity = 5

    Output:
        False

Example 3:
    Input:
        jug1Capacity = 1
        jug2Capacity = 2
        targetCapacity = 3

    Output:
        True

Constraints:
    1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
'''

# Math + Greatest Common Divisor

from math import gcd


class Solution:
    def canMeasureWater(
        self,
        jug1Capacity: int,
        jug2Capacity: int,
        targetCapacity: int
    ) -> bool:

        if targetCapacity > jug1Capacity + jug2Capacity:
            return False

        if targetCapacity == 0:
            return True

        return targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0


# Example usage
solution = Solution()

# Example 1
print(solution.canMeasureWater(3, 5, 4))
# Output: True

# Example 2
print(solution.canMeasureWater(2, 6, 5))
# Output: False

# Example 3
print(solution.canMeasureWater(1, 2, 3))
# Output: True

# Example 4
print(solution.canMeasureWater(6, 10, 8))
# Output: True

# Example 5
print(solution.canMeasureWater(4, 6, 5))
# Output: False

# Example 6
print(solution.canMeasureWater(8, 12, 20))
# Output: True
