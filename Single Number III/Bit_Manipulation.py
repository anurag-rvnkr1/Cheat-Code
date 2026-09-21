'''
260. Single Number III

Given an integer array nums, in which exactly two elements appear only once
and all the other elements appear exactly twice, find the two elements that
appear only once.

Return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses
only constant extra space.

Example 1:
    Input: nums = [1,2,1,3,2,5]
    Output: [3,5]

Explanation:
    The numbers 3 and 5 appear exactly once.

Example 2:
    Input: nums = [-1,0]
    Output: [-1,0]

Example 3:
    Input: nums = [0,1]
    Output: [1,0]

Constraints:
    2 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Exactly two integers appear once and all others appear twice.
'''

# Bit Manipulation

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0

        # XOR of the two unique numbers.
        for num in nums:
            xor_all ^= num

        # Rightmost set bit that differs between the two unique numbers.
        rightmost_set_bit = xor_all & -xor_all

        first = 0
        second = 0

        # Split numbers into two groups based on the set bit.
        for num in nums:
            if num & rightmost_set_bit:
                first ^= num
            else:
                second ^= num

        return [first, second]


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 1, 3, 2, 5]
print(solution.singleNumber(nums1))
# Output: [3, 5]

# Example 2
nums2 = [-1, 0]
print(solution.singleNumber(nums2))
# Output: [-1, 0]

# Example 3
nums3 = [0, 1]
print(solution.singleNumber(nums3))
# Output: [1, 0]

# Example 4
nums4 = [4, 1, 2, 1, 2, 5]
print(solution.singleNumber(nums4))
# Output: [4, 5]
