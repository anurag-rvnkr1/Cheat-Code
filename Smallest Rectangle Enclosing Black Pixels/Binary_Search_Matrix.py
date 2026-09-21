'''
302. Smallest Rectangle Enclosing Black Pixels

You are given an m x n binary image represented by strings "0" (white pixel)
and "1" (black pixel).

The black pixels form one connected region.

You are also given the coordinates (x, y) of one black pixel.

Return the area of the smallest axis-aligned rectangle that encloses all
black pixels.

Example 1:
    Input:
        image = [
            "0010",
            "0110",
            "0100"
        ]
        x = 0
        y = 2

    Output:
        6

Explanation:
        Smallest rectangle:
            Rows    : 0 to 2
            Columns : 1 to 2

        Area = 3 × 2 = 6

Example 2:
    Input:
        image = ["1"]
        x = 0
        y = 0

    Output:
        1

Constraints:
    m == image.length
    n == image[i].length
    1 <= m, n <= 100
    image[i][j] is either '0' or '1'.
    The black pixels form one connected component.

Follow-up:
    Solve it in O(m log n + n log m).
'''

# Binary Search + Matrix

from typing import List


class Solution:
    def minArea(self, image: List[str], x: int, y: int) -> int:
        rows = len(image)
        cols = len(image[0])

        # Check whether a row contains a black pixel.
        def row_has_black(row: int) -> bool:
            for col in range(cols):
                if image[row][col] == "1":
                    return True
            return False

        # Check whether a column contains a black pixel.
        def col_has_black(col: int) -> bool:
            for row in range(rows):
                if image[row][col] == "1":
                    return True
            return False

        # Binary search top boundary.
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if row_has_black(mid):
                right = mid
            else:
                left = mid + 1
        top = left

        # Binary search bottom boundary.
        left, right = x, rows - 1
        while left < right:
            mid = (left + right + 1) // 2
            if row_has_black(mid):
                left = mid
            else:
                right = mid - 1
        bottom = left

        # Binary search left boundary.
        left, right = 0, y
        while left < right:
            mid = (left + right) // 2
            if col_has_black(mid):
                right = mid
            else:
                left = mid + 1
        left_boundary = left

        # Binary search right boundary.
        left, right = y, cols - 1
        while left < right:
            mid = (left + right + 1) // 2
            if col_has_black(mid):
                left = mid
            else:
                right = mid - 1
        right_boundary = left

        return (
            (bottom - top + 1) *
            (right_boundary - left_boundary + 1)
        )


# Example usage
solution = Solution()

# Example 1
image1 = [
    "0010",
    "0110",
    "0100"
]

print(solution.minArea(image1, 0, 2))
# Output: 6

# Example 2
image2 = ["1"]

print(solution.minArea(image2, 0, 0))
# Output: 1

# Example 3
image3 = [
    "00000",
    "00100",
    "01110",
    "00100",
    "00000"
]

print(solution.minArea(image3, 2, 2))
# Output: 9

# Example 4
image4 = [
    "111",
    "111"
]

print(solution.minArea(image4, 0, 1))
# Output: 6
