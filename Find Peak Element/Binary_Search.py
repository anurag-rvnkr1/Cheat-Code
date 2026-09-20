'''
162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2

Explanation:
    3 is a peak element and your function should return index 2.

Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5

Explanation:
    Your function can return either index 1 or index 5,
    where the peak elements are 2 and 6.

Constraints:
    1 <= nums.length <= 1000
    -2^31 <= nums[i] <= 2^31 - 1
    nums[i] != nums[i + 1] for all valid i.
'''

# Binary Search

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                # Peak is at mid or to the left.
                right = mid
            else:
                # Peak is to the right.
                left = mid + 1

        return left


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
print(solution.findPeakElement(nums1))  # Output: 2

# Example 2
nums2 = [1, 2, 1, 3, 5, 6, 4]
print(solution.findPeakElement(nums2))  # Output: 5 (or 1)

# Example 3
nums3 = [1]
print(solution.findPeakElement(nums3))  # Output: 0

# Example 4
nums4 = [1, 2]
print(solution.findPeakElement(nums4))  # Output: 1
