'''
213. House Robber II

You are a professional robber planning to rob houses along a street.
All houses are arranged in a circle, which means the first house is adjacent
to the last house.

You cannot rob two adjacent houses.

Given an integer array nums representing the amount of money in each house,
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: nums = [2,3,2]
    Output: 3

Explanation:
    You cannot rob house 1 and house 3 because they are adjacent.

Example 2:
    Input: nums = [1,2,3,1]
    Output: 4

Explanation:
    Rob house 1 and house 3 for a total of 4.

Example 3:
    Input: nums = [1,2,3]
    Output: 3

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 1000
'''

# Dynamic Programming

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Helper function for the linear House Robber problem.
        def robLinear(houses: List[int]) -> int:
            prev2 = 0
            prev1 = 0

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1: Exclude the last house.
        # Case 2: Exclude the first house.
        return max(
            robLinear(nums[:-1]),
            robLinear(nums[1:])
        )


# Example usage
solution = Solution()

# Example 1
nums1 = [2, 3, 2]
print(solution.rob(nums1))  # Output: 3

# Example 2
nums2 = [1, 2, 3, 1]
print(solution.rob(nums2))  # Output: 4

# Example 3
nums3 = [1, 2, 3]
print(solution.rob(nums3))  # Output: 3

# Example 4
nums4 = [5]
print(solution.rob(nums4))  # Output: 5
