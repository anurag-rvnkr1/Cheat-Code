'''
416. Partition Equal Subset Sum

Given an integer array nums, return True if you can partition the array into
two subsets such that the sum of the elements in both subsets is equal.

Example 1:
    Input:
        nums = [1,5,11,5]

    Output:
        True

Explanation:
        The array can be partitioned as [1,5,5] and [11].

Example 2:
    Input:
        nums = [1,2,3,5]

    Output:
        False

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 100
'''

# Dynamic Programming (0/1 Knapsack)

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for number in nums:
            for current_sum in range(target, number - 1, -1):
                dp[current_sum] = (
                    dp[current_sum] or
                    dp[current_sum - number]
                )

        return dp[target]


# Example usage
solution = Solution()

# Example 1
nums1 = [1,5,11,5]
print(solution.canPartition(nums1))
# Output: True

# Example 2
nums2 = [1,2,3,5]
print(solution.canPartition(nums2))
# Output: False

# Example 3
nums3 = [2,2,1,1]
print(solution.canPartition(nums3))
# Output: True

# Example 4
nums4 = [3,3,3,4,5]
print(solution.canPartition(nums4))
# Output: True

# Example 5
nums5 = [2,3,5,9]
print(solution.canPartition(nums5))
# Output: False

# Example 6
nums6 = [100,100]
print(solution.canPartition(nums6))
# Output: True
