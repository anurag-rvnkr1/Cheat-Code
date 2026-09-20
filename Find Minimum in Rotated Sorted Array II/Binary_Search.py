'''
154. Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Unlike Problem 153, this array may contain duplicate elements.

Given the sorted rotated array nums that may contain duplicates, return the minimum element.

You must decrease the overall operation steps as much as possible.

Example 1:
    Input: nums = [1,3,5]
    Output: 1

Example 2:
    Input: nums = [2,2,2,0,1]
    Output: 0

Example 3:
    Input: nums = [10,1,10,10,10]
    Output: 1

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    nums is sorted and rotated between 1 and n times.
'''

# Binary Search

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Minimum is in the right half.
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is at mid or in the left half.
                right = mid
            else:
                # Cannot determine the side because of duplicates.
                right -= 1

        return nums[left]


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 3, 5]
print(solution.findMin(nums1))  # Output: 1

# Example 2
nums2 = [2, 2, 2, 0, 1]
print(solution.findMin(nums2))  # Output: 0

# Example 3
nums3 = [10, 1, 10, 10, 10]
print(solution.findMin(nums3))  # Output: 1

# Example 4
nums4 = [3, 3, 1, 3]
print(solution.findMin(nums4))  # Output: 1
