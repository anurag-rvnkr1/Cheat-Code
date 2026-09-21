'''
280. Wiggle Sort

Given an integer array nums, reorder it in-place such that:

    nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] ...

This is called a wiggle sequence.

You may assume the input array always has a valid answer.

Example 1:
    Input: nums = [3,5,2,1,6,4]
    Output: [3,5,1,6,2,4]

Explanation:
    3 <= 5 >= 1 <= 6 >= 2 <= 4

Example 2:
    Input: nums = [6,6,5,6,3,8]
    Output: [6,6,5,6,3,8]

Explanation:
    6 <= 6 >= 5 <= 6 >= 3 <= 8

Constraints:
    1 <= nums.length <= 5 * 10^4
    0 <= nums[i] <= 10^4

Follow-up:
    Can you do it in O(n) time and in-place?
'''

# Greedy + Array

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything.
        Modify nums in-place.
        """

        for i in range(len(nums) - 1):

            # Even index: nums[i] should be <= nums[i + 1]
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

            # Odd index: nums[i] should be >= nums[i + 1]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 5, 2, 1, 6, 4]
solution.wiggleSort(nums1)
print(nums1)
# Output: [3, 5, 1, 6, 2, 4]

# Example 2
nums2 = [6, 6, 5, 6, 3, 8]
solution.wiggleSort(nums2)
print(nums2)
# Output: [6, 6, 5, 6, 3, 8]

# Example 3
nums3 = [1, 2, 3, 4, 5]
solution.wiggleSort(nums3)
print(nums3)
# Output: [1, 3, 2, 5, 4]

# Example 4
nums4 = [9, 8, 7, 6, 5, 4]
solution.wiggleSort(nums4)
print(nums4)
# Output: [8, 9, 6, 7, 4, 5]

# Example 5
nums5 = [1, 1, 1, 1]
solution.wiggleSort(nums5)
print(nums5)
# Output: [1, 1, 1, 1]
