'''
152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6

Explanation:
    The subarray [2,3] has the largest product 6.

Example 2:
    Input: nums = [-2,0,-1]
    Output: 0

Explanation:
    The result cannot be 2 because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit
    in a 32-bit integer.
'''

# Dynamic Programming

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Negative number swaps maximum and minimum products.
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product


# Example usage
solution = Solution()

# Example 1
nums1 = [2, 3, -2, 4]
print(solution.maxProduct(nums1))  # Output: 6

# Example 2
nums2 = [-2, 0, -1]
print(solution.maxProduct(nums2))  # Output: 0

# Example 3
nums3 = [-2, 3, -4]
print(solution.maxProduct(nums3))  # Output: 24

# Example 4
nums4 = [0, 2]
print(solution.maxProduct(nums4))  # Output: 2
