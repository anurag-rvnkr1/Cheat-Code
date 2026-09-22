'''
368. Largest Divisible Subset

Given a set of distinct positive integers nums, return the largest subset
such that every pair (answer[i], answer[j]) satisfies:

    answer[i] % answer[j] == 0
    or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Example 1:
    Input:
        nums = [1,2,3]

    Output:
        [1,2]

Example 2:
    Input:
        nums = [1,2,4,8]

    Output:
        [1,2,4,8]

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 10^9
    All integers in nums are unique.
'''

# Dynamic Programming + Longest Increasing Subsequence Style

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = [-1] * n

        max_length = 1
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_length:
                max_length = dp[i]
                max_index = i

        result = []

        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]

        return result[::-1]


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3]
print(solution.largestDivisibleSubset(nums1))
# Output: [1,2]

# Example 2
nums2 = [1,2,4,8]
print(solution.largestDivisibleSubset(nums2))
# Output: [1,2,4,8]

# Example 3
nums3 = [3,4,16,8]
print(solution.largestDivisibleSubset(nums3))
# Output: [4,8,16]

# Example 4
nums4 = [5,9,18,54,108]
print(solution.largestDivisibleSubset(nums4))
# Output: [9,18,54,108]

# Example 5
nums5 = [2,3,6,12,24]
print(solution.largestDivisibleSubset(nums5))
# Output: [2,6,12,24]

# Example 6
nums6 = [1,17,34,68,136,272]
print(solution.largestDivisibleSubset(nums6))
# Output: [1,17,34,68,136,272]
