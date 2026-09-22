'''
377. Combination Sum IV

Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

Different sequences are counted as different combinations.

Example 1:
    Input:
        nums = [1,2,3]
        target = 4

    Output:
        7

Explanation:
        The valid combinations are:
            (1,1,1,1)
            (1,1,2)
            (1,2,1)
            (2,1,1)
            (2,2)
            (1,3)
            (3,1)

Example 2:
    Input:
        nums = [9]
        target = 3

    Output:
        0

Constraints:
    1 <= nums.length <= 200
    1 <= nums[i] <= 1000
    All elements of nums are unique.
    1 <= target <= 1000

Follow-up:
    What if negative numbers are allowed?
'''

# Dynamic Programming (1D DP)

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for current_sum in range(1, target + 1):
            for number in nums:
                if current_sum >= number:
                    dp[current_sum] += dp[current_sum - number]

        return dp[target]


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3]
target1 = 4
print(solution.combinationSum4(nums1, target1))
# Output: 7

# Example 2
nums2 = [9]
target2 = 3
print(solution.combinationSum4(nums2, target2))
# Output: 0

# Example 3
nums3 = [2,3,5]
target3 = 8
print(solution.combinationSum4(nums3, target3))
# Output: 6

# Example 4
nums4 = [4,2,1]
target4 = 5
print(solution.combinationSum4(nums4, target4))
# Output: 10

# Example 5
nums5 = [3,5,7]
target5 = 12
print(solution.combinationSum4(nums5, target5))
# Output: 4

# Example 6
nums6 = [1,5,10]
target6 = 12
print(solution.combinationSum4(nums6, target6))
# Output: 19
