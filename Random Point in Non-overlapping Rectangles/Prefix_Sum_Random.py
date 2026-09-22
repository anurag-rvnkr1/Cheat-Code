'''
497. Random Point in Non-overlapping Rectangles

You are given an array of non-overlapping axis-aligned rectangles.

Each rectangle is represented as:

    [x1, y1, x2, y2]

where all integer points inside the rectangle (including boundaries)
are valid.

Implement:

    Solution(rects)
        Initializes the rectangles.

    pick()
        Returns a uniformly random integer point from all rectangles.

Each valid integer point across all rectangles must have equal probability.

Example 1:
    Input:
        rects = [[-2,-2,1,1],[2,2,4,6]]

    Output:
        Random integer point from either rectangle.

Constraints:
    1 <= rects.length <= 100
    rects[i].length == 4
    Rectangles do not overlap.
    pick() will be called at most 10^4 times.
'''

# Prefix Sum + Random Sampling + Binary Search

from typing import List
import random
import bisect


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rectangles = rects
        self.prefix_points = []
        total_points = 0

        for x1, y1, x2, y2 in rects:
            points_inside = (x2 - x1 + 1) * (y2 - y1 + 1)
            total_points += points_inside
            self.prefix_points.append(total_points)

        self.total_points = total_points

    def pick(self) -> List[int]:
        random_point = random.randint(1, self.total_points)

        rectangle_index = bisect.bisect_left(
            self.prefix_points,
            random_point
        )

        x1, y1, x2, y2 = self.rectangles[rectangle_index]

        previous_prefix = (
            self.prefix_points[rectangle_index - 1]
            if rectangle_index > 0
            else 0
        )

        offset = random_point - previous_prefix - 1

        width = x2 - x1 + 1

        x = x1 + (offset % width)
        y = y1 + (offset // width)

        return [x, y]


# Example usage
solution = Solution([
    [-2,-2,1,1],
    [2,2,4,6]
])

# Example 1
print(solution.pick())
# Output: Random integer point.

# Example 2
print(solution.pick())
# Output: Random integer point.

# Example 3
print(solution.pick())
# Output: Random integer point.

# Example 4
solution2 = Solution([[0,0,0,0]])
print(solution2.pick())
# Output: [0,0]

# Example 5
solution3 = Solution([[1,1,3,3]])
print(solution3.pick())
# Output: Random point from the 3x3 square.

# Example 6
solution4 = Solution([
    [0,0,1,1],
    [10,10,10,12],
    [-3,-3,-1,-1]
])

for _ in range(5):
    print(solution4.pick())
# Output: Random points from all rectangles with equal probability.
