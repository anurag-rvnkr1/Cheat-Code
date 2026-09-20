'''
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between
1 and n times.

For example:
    [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2]

Given the sorted rotated array nums of unique elements, return the minimum element.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [3,4,5,1,2]
    Output: 1

Example 2:
    Input: nums = [4,5,6,7,0,1,2]
    Output: 0

Example 3:
    Input: nums = [11,13,15,17]
    Output: 11

Constraints:
    n == nums.length
    1 <= n <= 5000
    -5000 <= nums[i] <= 5000
    All the integers of nums are unique.
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

            # Minimum is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is at mid or in the left half.
                right = mid

        return nums[left]


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 4, 5, 1, 2]
print(solution.findMin(nums1))  # Output: 1

# Example 2
nums2 = [4, 5, 6, 7, 0, 1, 2]
print(solution.findMin(nums2))  # Output: 0

# Example 3
nums3 = [11, 13, 15, 17]
print(solution.findMin(nums3))  # Output: 11

# Example 4
nums4 = [2, 1]
print(solution.findMin(nums4))  # Output: 1
