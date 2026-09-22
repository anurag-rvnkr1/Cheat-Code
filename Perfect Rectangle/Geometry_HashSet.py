'''
391. Perfect Rectangle

Given an array rectangles where rectangles[i] = [x1, y1, x2, y2]
represents an axis-aligned rectangle.

Return True if all rectangles together form exactly one perfect rectangle
(without overlaps and without gaps).

Example 1:
    Input:
        rectangles = [
            [1,1,3,3],
            [3,1,4,2],
            [3,2,4,4],
            [1,3,2,4],
            [2,3,3,4]
        ]

    Output:
        True

Example 2:
    Input:
        rectangles = [
            [1,1,2,3],
            [1,3,2,4],
            [3,1,4,2],
            [3,2,4,4]
        ]

    Output:
        False

Example 3:
    Input:
        rectangles = [
            [1,1,3,3],
            [3,1,4,2],
            [1,3,2,4],
            [2,2,4,4]
        ]

    Output:
        False

Constraints:
    1 <= rectangles.length <= 2 * 10^4
    rectangles[i].length == 4
    -10^5 <= x1 < x2 <= 10^5
    -10^5 <= y1 < y2 <= 10^5
'''

# Geometry + HashSet

from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()

        min_x = float("inf")
        min_y = float("inf")
        max_x = float("-inf")
        max_y = float("-inf")

        total_area = 0

        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)

            total_area += (x2 - x1) * (y2 - y1)

            rectangle_corners = [
                (x1, y1),
                (x1, y2),
                (x2, y1),
                (x2, y2)
            ]

            for corner in rectangle_corners:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        expected_corners = {
            (min_x, min_y),
            (min_x, max_y),
            (max_x, min_y),
            (max_x, max_y)
        }

        expected_area = (max_x - min_x) * (max_y - min_y)

        return (
            total_area == expected_area and
            corners == expected_corners
        )


# Example usage
solution = Solution()

# Example 1
rectangles1 = [
    [1,1,3,3],
    [3,1,4,2],
    [3,2,4,4],
    [1,3,2,4],
    [2,3,3,4]
]
print(solution.isRectangleCover(rectangles1))
# Output: True

# Example 2
rectangles2 = [
    [1,1,2,3],
    [1,3,2,4],
    [3,1,4,2],
    [3,2,4,4]
]
print(solution.isRectangleCover(rectangles2))
# Output: False

# Example 3
rectangles3 = [
    [1,1,3,3],
    [3,1,4,2],
    [1,3,2,4],
    [2,2,4,4]
]
print(solution.isRectangleCover(rectangles3))
# Output: False

# Example 4
rectangles4 = [
    [0,0,1,1],
    [1,0,2,1],
    [0,1,1,2],
    [1,1,2,2]
]
print(solution.isRectangleCover(rectangles4))
# Output: True

# Example 5
rectangles5 = [
    [0,0,2,1],
    [0,1,1,2],
    [1,1,2,2],
    [2,0,3,2]
]
print(solution.isRectangleCover(rectangles5))
# Output: True

# Example 6
rectangles6 = [
    [0,0,2,2],
    [1,1,3,3]
]
print(solution.isRectangleCover(rectangles6))
# Output: False
