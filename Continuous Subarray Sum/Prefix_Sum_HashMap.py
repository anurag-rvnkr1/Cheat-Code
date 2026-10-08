"""
523. Continuous Subarray Sum

Given an integer array nums and an integer k, return True if nums has
a continuous subarray of size at least two whose elements sum up to a
multiple of k.

An integer x is a multiple of k if there exists an integer n such that
x = n * k.

Examples:
1. Input: nums = [23, 2, 4, 6, 7], k = 6
   Output: True

2. Input: nums = [23, 2, 6, 4, 7], k = 6
   Output: True

3. Input: nums = [23, 2, 6, 4, 7], k = 13
   Output: False

4. Input: nums = [5, 0, 0, 0], k = 3
   Output: True

5. Input: nums = [1, 2, 3], k = 5
   Output: True

6. Input: nums = [1, 0], k = 2
   Output: False
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_index = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum

            if remainder in remainder_index:
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                remainder_index[remainder] = i

        return False


# Example 1
nums = [23, 2, 4, 6, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))  # True

# Example 2
nums = [23, 2, 6, 4, 7]
k = 6
print(Solution().checkSubarraySum(nums, k))  # True

# Example 3
nums = [23, 2, 6, 4, 7]
k = 13
print(Solution().checkSubarraySum(nums, k))  # False

# Example 4
nums = [5, 0, 0, 0]
k = 3
print(Solution().checkSubarraySum(nums, k))  # True

# Example 5
nums = [1, 2, 3]
k = 5
print(Solution().checkSubarraySum(nums, k))  # True

# Example 6
nums = [1, 0]
k = 2
print(Solution().checkSubarraySum(nums, k))  # False


# Time Complexity: O(n)
# Space Complexity: O(n)
