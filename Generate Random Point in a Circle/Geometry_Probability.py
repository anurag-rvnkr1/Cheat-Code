'''
478. Generate Random Point in a Circle

Given the radius and center of a circle, implement the Solution class.

Functions:
    Solution(radius, x_center, y_center)
        Initializes the circle.

    randPoint()
        Returns a uniformly random point inside the circle.

Every point inside the circle should have equal probability of being returned.

Example 1:
    Input:
        ["Solution","randPoint","randPoint","randPoint"]
        [[1.0,0.0,0.0],[],[],[]]

    Output:
        Random points inside the unit circle.

Constraints:
    0 < radius <= 10^8
    -10^7 <= x_center, y_center <= 10^7
    At most 3 * 10^4 calls to randPoint().
'''

# Geometry + Probability (Polar Coordinates)

import random
import math
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        # Random angle between 0 and 2π.
        angle = random.uniform(0, 2 * math.pi)

        # sqrt(random()) ensures uniform area distribution.
        distance = self.radius * math.sqrt(random.random())

        x = self.x_center + distance * math.cos(angle)
        y = self.y_center + distance * math.sin(angle)

        return [x, y]


# Example usage
solution = Solution(1.0, 0.0, 0.0)

# Example 1
print(solution.randPoint())
# Output: Random point inside unit circle.

# Example 2
print(solution.randPoint())
# Output: Random point inside unit circle.

# Example 3
print(solution.randPoint())
# Output: Random point inside unit circle.

# Example 4
solution2 = Solution(5.0, 2.0, 3.0)
print(solution2.randPoint())
# Output: Random point inside circle centered at (2,3).

# Example 5
solution3 = Solution(10.0, -5.0, 8.0)
print(solution3.randPoint())
# Output: Random point inside large circle.

# Example 6
# Generate multiple random points.
points = [solution.randPoint() for _ in range(5)]
print(points)
# Output: Five uniformly distributed random points.
