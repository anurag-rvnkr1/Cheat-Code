'''
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]

Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1

Follow-up:
    Could you minimize the total number of operations?
'''

# Two Pointers + Array

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything.
        Modify nums in-place.
        """

        left = 0

        # Move all non-zero elements forward.
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


# Example usage
solution = Solution()

# Example 1
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1)
# Output: [1, 3, 12, 0, 0]

# Example 2
nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)
# Output: [0]

# Example 3
nums3 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
solution.moveZeroes(nums3)
print(nums3)
# Output: [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]

# Example 4
nums4 = [1, 2, 3, 4]
solution.moveZeroes(nums4)
print(nums4)
# Output: [1, 2, 3, 4]

# Example 5
nums5 = [0, 0, 0, 1]
solution.moveZeroes(nums5)
print(nums5)
# Output: [1, 0, 0, 0]
