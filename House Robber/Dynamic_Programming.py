'''
198. House Robber

You are a professional robber planning to rob houses along a street.

Each house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security systems
connected and automatically contact the police if two adjacent houses are broken
into on the same night.

Given an integer array nums representing the amount of money at each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 4

Explanation:
    Rob house 1 (money = 1) and house 3 (money = 3).
    Total amount = 4.

Example 2:
    Input: nums = [2,7,9,3,1]
    Output: 12

Explanation:
    Rob house 1 (money = 2), house 3 (money = 9),
    and house 5 (money = 1).
    Total amount = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400
'''

# Dynamic Programming

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # prev2 = Maximum money up to house i-2.
        # prev1 = Maximum money up to house i-1.
        prev2 = 0
        prev1 = 0

        for money in nums:
            current = max(prev1, prev2 + money)
            prev2 = prev1
            prev1 = current

        return prev1


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
print(solution.rob(nums1))  # Output: 4

# Example 2
nums2 = [2, 7, 9, 3, 1]
print(solution.rob(nums2))  # Output: 12

# Example 3
nums3 = [2, 1, 1, 2]
print(solution.rob(nums3))  # Output: 4

# Example 4
nums4 = [5]
print(solution.rob(nums4))  # Output: 5
