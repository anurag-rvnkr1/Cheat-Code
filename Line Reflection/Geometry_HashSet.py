'''
356. Line Reflection

Given n points on a 2D plane, find if there exists a vertical line
that reflects the points symmetrically.

Return True if such a line exists, otherwise False.

Example 1:
    Input:
        points = [[1,1],[-1,1]]

    Output:
        True

Example 2:
    Input:
        points = [[1,1],[-1,-1]]

    Output:
        False

Constraints:
    1 <= points.length <= 10^4
    points[i].length == 2
    -10^8 <= xi, yi <= 10^8
'''

# Geometry + HashSet

from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        point_set = set()
        minimum_x = float("inf")
        maximum_x = float("-inf")

        for x, y in points:
            point_set.add((x, y))
            minimum_x = min(minimum_x, x)
            maximum_x = max(maximum_x, x)

        reflection_sum = minimum_x + maximum_x

        for x, y in point_set:
            if (reflection_sum - x, y) not in point_set:
                return False

        return True


# Example usage
solution = Solution()

# Example 1
points1 = [[1,1],[-1,1]]
print(solution.isReflected(points1))
# Output: True

# Example 2
points2 = [[1,1],[-1,-1]]
print(solution.isReflected(points2))
# Output: False

# Example 3
points3 = [[0,0],[2,0],[1,1]]
print(solution.isReflected(points3))
# Output: True

# Example 4
points4 = [[0,0],[1,0],[2,0]]
print(solution.isReflected(points4))
# Output: True

# Example 5
points5 = [[2,3],[4,3],[3,5],[3,1]]
print(solution.isReflected(points5))
# Output: True

# Example 6
points6 = [[1,2],[3,2],[2,3],[4,3]]
print(solution.isReflected(points6))
# Output: False
