'''
335. Self Crossing

You are given an array distance where distance[i] represents the distance moved
during the ith move.

You start at (0,0) facing north.

Movement pattern repeats counter-clockwise:
    North -> West -> South -> East -> North ...

Return True if your path crosses itself at any point.

Example 1:
    Input:
        distance = [2,1,1,2]

    Output:
        True

Example 2:
    Input:
        distance = [1,2,3,4]

    Output:
        False

Example 3:
    Input:
        distance = [1,1,1,2,1]

    Output:
        True

Constraints:
    1 <= distance.length <= 10^5
    1 <= distance[i] <= 10^5
'''

# Geometry + Simulation

from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)

        for i in range(3, n):

            # Case 1: Current line crosses the line 3 steps ahead.
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: Current line overlaps the line 4 steps ahead.
            if (
                i >= 4 and
                distance[i - 1] == distance[i - 3] and
                distance[i] + distance[i - 4] >= distance[i - 2]
            ):
                return True

            # Case 3: Current line crosses the line 5 steps ahead.
            if (
                i >= 5 and
                distance[i - 2] >= distance[i - 4] and
                distance[i] >= distance[i - 2] - distance[i - 4] and
                distance[i - 1] >= distance[i - 3] - distance[i - 5] and
                distance[i - 1] <= distance[i - 3]
            ):
                return True

        return False


# Example usage
solution = Solution()

# Example 1
distance1 = [2,1,1,2]
print(solution.isSelfCrossing(distance1))
# Output: True

# Example 2
distance2 = [1,2,3,4]
print(solution.isSelfCrossing(distance2))
# Output: False

# Example 3
distance3 = [1,1,1,2,1]
print(solution.isSelfCrossing(distance3))
# Output: True

# Example 4
distance4 = [3,3,4,2,2]
print(solution.isSelfCrossing(distance4))
# Output: False

# Example 5
distance5 = [1,1,2,1,1]
print(solution.isSelfCrossing(distance5))
# Output: True

# Example 6
distance6 = [1,2,2,1,1]
print(solution.isSelfCrossing(distance6))
# Output: True
