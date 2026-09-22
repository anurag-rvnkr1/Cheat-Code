'''
325. Maximum Size Subarray Sum Equals k

Given an integer array nums and an integer k, return the maximum length of a
subarray that sums to k.

If there isn't one, return 0.

Example 1:
    Input:
        nums = [1,-1,5,-2,3]
        k = 3

    Output:
        4

Explanation:
        [1,-1,5,-2] sums to 3.

Example 2:
    Input:
        nums = [-2,-1,2,1]
        k = 1

    Output:
        2

Explanation:
        [-1,2] sums to 1.

Constraints:
    1 <= nums.length <= 2 * 10^5
    -10^4 <= nums[i] <= 10^4
    -10^9 <= k <= 10^9
'''

# Prefix Sum + HashMap

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_index = {0: -1}  # Prefix sum -> earliest index

        prefix_sum = 0
        maximum_length = 0

        for index, number in enumerate(nums):
            prefix_sum += number

            # If (prefix_sum - k) exists, subarray sums to k.
            if prefix_sum - k in prefix_index:
                maximum_length = max(
                    maximum_length,
                    index - prefix_index[prefix_sum - k]
                )

            # Store earliest occurrence only.
            if prefix_sum not in prefix_index:
                prefix_index[prefix_sum] = index

        return maximum_length


# Example usage
solution = Solution()

# Example 1
nums1 = [1, -1, 5, -2, 3]
k1 = 3
print(solution.maxSubArrayLen(nums1, k1))
# Output: 4

# Example 2
nums2 = [-2, -1, 2, 1]
k2 = 1
print(solution.maxSubArrayLen(nums2, k2))
# Output: 2

# Example 3
nums3 = [1, 2, 3]
k3 = 6
print(solution.maxSubArrayLen(nums3, k3))
# Output: 3

# Example 4
nums4 = [2, -2, 2, -2]
k4 = 0
print(solution.maxSubArrayLen(nums4, k4))
# Output: 4

# Example 5
nums5 = [5, 1, -1, 5]
k5 = 5
print(solution.maxSubArrayLen(nums5, k5))
# Output: 3

# Example 6
nums6 = [3, -3, 3, -3, 3]
k6 = 3
print(solution.maxSubArrayLen(nums6, k6))
# Output: 5
