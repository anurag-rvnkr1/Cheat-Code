'''
492. Construct the Rectangle

A web developer needs to design a rectangular page.

Given an integer area, find the dimensions [L, W] such that:

    - L * W = area
    - L >= W
    - L - W is minimized

Return [L, W].

Example 1:
    Input:
        area = 4

    Output:
        [2,2]

Example 2:
    Input:
        area = 37

    Output:
        [37,1]

Example 3:
    Input:
        area = 122122

    Output:
        [427,286]

Constraints:
    1 <= area <= 10^7
'''

# Math

from typing import List
import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(math.sqrt(area))

        while area % width != 0:
            width -= 1

        length = area // width

        return [length, width]


# Example usage
solution = Solution()

# Example 1
area1 = 4
print(solution.constructRectangle(area1))
# Output: [2,2]

# Example 2
area2 = 37
print(solution.constructRectangle(area2))
# Output: [37,1]

# Example 3
area3 = 122122
print(solution.constructRectangle(area3))
# Output: [427,286]

# Example 4
area4 = 36
print(solution.constructRectangle(area4))
# Output: [6,6]

# Example 5
area5 = 9999991
print(solution.constructRectangle(area5))
# Output: [9999991,1]

# Example 6
area6 = 100
print(solution.constructRectangle(area6))
# Output: [10,10]
