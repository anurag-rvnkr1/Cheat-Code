'''
494. Target Sum

You are given an integer array nums and an integer target.

Assign either '+' or '-' before every number so that the resulting expression
equals target.

Return the number of different expressions that evaluate to target.

Example 1:
    Input:
        nums = [1,1,1,1,1]
        target = 3

    Output:
        5

Explanation:
        There are 5 ways to assign '+' and '-' signs.

Example 2:
    Input:
        nums = [1]
        target = 1

    Output:
        1

Constraints:
    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
'''

# Dynamic Programming + 0/1 Knapsack (Subset Sum)

from typing import List


class Solution:
    def findTargetSumWays(
        self,
        nums: List[int],
        target: int
    ) -> int:

        total_sum = sum(nums)

        # Impossible case.
        if abs(target) > total_sum:
            return 0

        # Transform to subset sum.
        if (total_sum + target) % 2 != 0:
            return 0

        subset_sum = (total_sum + target) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for number in nums:
            for current_sum in range(subset_sum, number - 1, -1):
                dp[current_sum] += dp[current_sum - number]

        return dp[subset_sum]


# Example usage
solution = Solution()

# Example 1
nums1 = [1,1,1,1,1]
target1 = 3
print(solution.findTargetSumWays(nums1, target1))
# Output: 5

# Example 2
nums2 = [1]
target2 = 1
print(solution.findTargetSumWays(nums2, target2))
# Output: 1

# Example 3
nums3 = [1,2,1]
target3 = 0
print(solution.findTargetSumWays(nums3, target3))
# Output: 2

# Example 4
nums4 = [0,0,0,0,1]
target4 = 1
print(solution.findTargetSumWays(nums4, target4))
# Output: 16

# Example 5
nums5 = [2,3,5,6,8,10]
target5 = 10
print(solution.findTargetSumWays(nums5, target5))
# Output: 1

# Example 6
nums6 = [100]
target6 = -200
print(solution.findTargetSumWays(nums6, target6))
# Output: 0
