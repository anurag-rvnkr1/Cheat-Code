'''
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting
some or no elements without changing the order of the remaining elements.

Example 1:
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4

Explanation:
    The longest increasing subsequence is [2,3,7,101].

Example 2:
    Input: nums = [0,1,0,3,2,3]
    Output: 4

Example 3:
    Input: nums = [7,7,7,7,7,7,7]
    Output: 1

Constraints:
    1 <= nums.length <= 2500
    -10^4 <= nums[i] <= 10^4

Follow-up:
    Can you solve it in O(n log n) time complexity?
'''

# Dynamic Programming + Binary Search

from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for number in nums:
            position = bisect_left(tails, number)

            if position == len(tails):
                tails.append(number)
            else:
                tails[position] = number

        return len(tails)


# Example usage
solution = Solution()

# Example 1
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.lengthOfLIS(nums1))
# Output: 4

# Example 2
nums2 = [0, 1, 0, 3, 2, 3]
print(solution.lengthOfLIS(nums2))
# Output: 4

# Example 3
nums3 = [7, 7, 7, 7, 7, 7, 7]
print(solution.lengthOfLIS(nums3))
# Output: 1

# Example 4
nums4 = [4, 10, 4, 3, 8, 9]
print(solution.lengthOfLIS(nums4))
# Output: 3

# Example 5
nums5 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(solution.lengthOfLIS(nums5))
# Output: 6

# Example 6
nums6 = [2, 2, 2, 2]
print(solution.lengthOfLIS(nums6))
# Output: 1
