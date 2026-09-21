'''
223. Rectangle Area

Given the coordinates of two rectilinear rectangles in a 2D plane,
return the total area covered by the two rectangles.

The first rectangle is defined by:
    (ax1, ay1) -> bottom-left corner
    (ax2, ay2) -> top-right corner

The second rectangle is defined by:
    (bx1, by1) -> bottom-left corner
    (bx2, by2) -> top-right corner

Example 1:
    Input:
        ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4
        bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
    Output: 45

Example 2:
    Input:
        ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2
        bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
    Output: 16

Constraints:
    -10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4
    ax1 < ax2
    ay1 < ay2
    bx1 < bx2
    by1 < by2
'''

# Geometry + Math


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int
    ) -> int:

        # Area of both rectangles.
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        # Width and height of overlapping rectangle.
        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))

        overlap_area = overlap_width * overlap_height

        return area_a + area_b - overlap_area


# Example usage
solution = Solution()

# Example 1
print(solution.computeArea(
    -3, 0, 3, 4,
    0, -1, 9, 2
))
# Output: 45

# Example 2
print(solution.computeArea(
    -2, -2, 2, 2,
    -2, -2, 2, 2
))
# Output: 16

# Example 3
print(solution.computeArea(
    0, 0, 2, 2,
    3, 3, 5, 5
))
# Output: 8

# Example 4
print(solution.computeArea(
    -2, -2, 2, 2,
    1, 1, 3, 3
))
# Output: 19
