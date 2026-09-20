'''
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4

    Explanation:
        The longest consecutive sequence is [1,2,3,4].
        Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Example 3:
    Input: nums = [1,0,1,2]
    Output: 3

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
'''

# Hash Set

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Start only from the beginning of a sequence.
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


# Example usage
solution = Solution()

# Example 1
nums1 = [100, 4, 200, 1, 3, 2]
print(solution.longestConsecutive(nums1))  # Output: 4

# Example 2
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(solution.longestConsecutive(nums2))  # Output: 9

# Example 3
nums3 = [1, 0, 1, 2]
print(solution.longestConsecutive(nums3))  # Output: 3
