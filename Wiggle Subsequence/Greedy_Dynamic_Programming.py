'''
376. Wiggle Subsequence

A wiggle sequence is a sequence where the differences between successive
numbers strictly alternate between positive and negative.

The first difference may be either positive or negative.

Given an integer array nums, return the length of the longest wiggle subsequence.

Example 1:
    Input:
        nums = [1,7,4,9,2,5]

    Output:
        6

Explanation:
        The entire sequence is a wiggle sequence.

Example 2:
    Input:
        nums = [1,17,5,10,13,15,10,5,16,8]

    Output:
        7

Example 3:
    Input:
        nums = [1,2,3,4,5,6,7,8,9]

    Output:
        2

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 1000

Follow-up:
    Can you solve it in O(n) time?
'''

# Greedy + Dynamic Programming

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        up = 1
        down = 1

        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                up = down + 1

            elif nums[index] < nums[index - 1]:
                down = up + 1

        return max(up, down)


# Example usage
solution = Solution()

# Example 1
nums1 = [1,7,4,9,2,5]
print(solution.wiggleMaxLength(nums1))
# Output: 6

# Example 2
nums2 = [1,17,5,10,13,15,10,5,16,8]
print(solution.wiggleMaxLength(nums2))
# Output: 7

# Example 3
nums3 = [1,2,3,4,5,6,7,8,9]
print(solution.wiggleMaxLength(nums3))
# Output: 2

# Example 4
nums4 = [3,3,3,2,5]
print(solution.wiggleMaxLength(nums4))
# Output: 3

# Example 5
nums5 = [0,0]
print(solution.wiggleMaxLength(nums5))
# Output: 1

# Example 6
nums6 = [1,3,2,4,3,5,4,6]
print(solution.wiggleMaxLength(nums6))
# Output: 8
