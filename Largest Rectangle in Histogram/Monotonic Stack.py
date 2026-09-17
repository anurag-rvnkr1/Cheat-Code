'''
84. Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
    Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation:
    The histogram has bar widths of 1.
    The largest rectangle has an area of 10 units.

Example 2:
    Input: heights = [2,4]
    Output: 4

Constraints:
    1 <= heights.length <= 10^5
    0 <= heights[i] <= 10^4
'''

# Monotonic Stack
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i, height in enumerate(heights):

            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]

                left = stack[-1] if stack else -1
                width = i - left - 1

                max_area = max(max_area, h * width)

            stack.append(i)

        # Process remaining bars
        n = len(heights)

        while stack:
            h = heights[stack.pop()]

            left = stack[-1] if stack else -1
            width = n - left - 1

            max_area = max(max_area, h * width)

        return max_area


# Example usage
solution = Solution()

print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Output: 10
print(solution.largestRectangleArea([2, 4]))  # Output: 4
print(solution.largestRectangleArea([2, 1, 2]))  # Output: 3
print(solution.largestRectangleArea([1, 1, 1, 1]))  # Output: 4
