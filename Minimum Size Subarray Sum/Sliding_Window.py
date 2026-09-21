'''
209. Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal
to target. If there is no such subarray, return 0 instead.

Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2

Explanation:
    The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

Constraints:
    1 <= target <= 10^9
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^4
'''

# Sliding Window

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        minimum_length = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink the window while the sum satisfies the target.
            while current_sum >= target:
                minimum_length = min(minimum_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if minimum_length == float("inf") else minimum_length


# Example usage
solution = Solution()

# Example 1
target1 = 7
nums1 = [2, 3, 1, 2, 4, 3]
print(solution.minSubArrayLen(target1, nums1))  # Output: 2

# Example 2
target2 = 4
nums2 = [1, 4, 4]
print(solution.minSubArrayLen(target2, nums2))  # Output: 1

# Example 3
target3 = 11
nums3 = [1, 1, 1, 1, 1, 1, 1, 1]
print(solution.minSubArrayLen(target3, nums3))  # Output: 0

# Example 4
target4 = 15
nums4 = [1, 2, 3, 4, 5]
print(solution.minSubArrayLen(target4, nums4))  # Output: 5
