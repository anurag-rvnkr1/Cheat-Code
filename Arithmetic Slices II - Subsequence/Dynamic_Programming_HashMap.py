'''
446. Arithmetic Slices II - Subsequence

Given an integer array nums, return the number of arithmetic subsequences of length
at least 3.

An arithmetic subsequence is a sequence where the difference between consecutive
elements is the same.

A subsequence is obtained by deleting some (possibly zero) elements without
changing the order of the remaining elements.

Example 1:
    Input:
        nums = [2,4,6,8,10]

    Output:
        7

Explanation:
        Arithmetic subsequences include:
        [2,4,6]
        [4,6,8]
        [6,8,10]
        [2,4,6,8]
        [4,6,8,10]
        [2,4,6,8,10]
        [2,6,10]

Example 2:
    Input:
        nums = [7,7,7,7,7]

    Output:
        16

Constraints:
    1 <= nums.length <= 1000
    -2^31 <= nums[i] <= 2^31 - 1
'''

# Dynamic Programming + HashMap

from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i][diff] = number of arithmetic subsequences ending at i
        dp = [defaultdict(int) for _ in range(n)]

        answer = 0

        for i in range(n):
            for j in range(i):
                difference = nums[i] - nums[j]

                previous = dp[j][difference]

                answer += previous

                dp[i][difference] += previous + 1

        return answer


# Example usage
solution = Solution()

# Example 1
nums1 = [2,4,6,8,10]
print(solution.numberOfArithmeticSlices(nums1))
# Output: 7

# Example 2
nums2 = [7,7,7,7,7]
print(solution.numberOfArithmeticSlices(nums2))
# Output: 16

# Example 3
nums3 = [1,2,3,4]
print(solution.numberOfArithmeticSlices(nums3))
# Output: 3

# Example 4
nums4 = [1,3,5,7,9]
print(solution.numberOfArithmeticSlices(nums4))
# Output: 7

# Example 5
nums5 = [1,5,9,13,17,21]
print(solution.numberOfArithmeticSlices(nums5))
# Output: 20

# Example 6
nums6 = [1,1,2,3,4]
print(solution.numberOfArithmeticSlices(nums6))
# Output: 2
