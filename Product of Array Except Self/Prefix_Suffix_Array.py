'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Explanation:
    answer[0] = 2 × 3 × 4 = 24
    answer[1] = 1 × 3 × 4 = 12
    answer[2] = 1 × 2 × 4 = 8
    answer[3] = 1 × 2 × 3 = 6

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    2 <= nums.length <= 10^5
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a
    32-bit integer.

Follow-up:
    Can you solve it in O(1) extra space?
'''

# Prefix & Suffix Array

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Prefix product
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4]
print(solution.productExceptSelf(nums1))
# Output: [24, 12, 8, 6]

# Example 2
nums2 = [-1, 1, 0, -3, 3]
print(solution.productExceptSelf(nums2))
# Output: [0, 0, 9, 0, 0]

# Example 3
nums3 = [2, 3, 4, 5]
print(solution.productExceptSelf(nums3))
# Output: [60, 40, 30, 24]

# Example 4
nums4 = [5, 2]
print(solution.productExceptSelf(nums4))
# Output: [2, 5]
