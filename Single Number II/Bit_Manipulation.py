'''
137. Single Number II

Given an integer array nums where every element appears three times except for one,
which appears exactly once.

Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant
extra space.

Example 1:
    Input: nums = [2,2,3,2]
    Output: 3

Example 2:
    Input: nums = [0,1,0,1,0,1,99]
    Output: 99

Example 3:
    Input: nums = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
    Output: -4

Constraints:
    1 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Each element in nums appears exactly three times except for one element
    which appears exactly once.
'''

# Bit Manipulation (Ones and Twos)

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones


# Example usage
solution = Solution()

# Example 1
nums1 = [2, 2, 3, 2]
print(solution.singleNumber(nums1))  # Output: 3

# Example 2
nums2 = [0, 1, 0, 1, 0, 1, 99]
print(solution.singleNumber(nums2))  # Output: 99

# Example 3
nums3 = [-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]
print(solution.singleNumber(nums3))  # Output: -4

# Example 4
nums4 = [5]
print(solution.singleNumber(nums4))  # Output: 5
