'''
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's
in the array.

Example 1:
    Input:
        nums = [1,1,0,1,1,1]

    Output:
        3

Explanation:
        The first two digits or the last three digits are consecutive 1s.
        The maximum number of consecutive 1s is 3.

Example 2:
    Input:
        nums = [1,0,1,1,0,1]

    Output:
        2

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
'''

# Array + Greedy

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum_consecutive_ones = 0
        current_consecutive_ones = 0

        for number in nums:
            if number == 1:
                current_consecutive_ones += 1
                maximum_consecutive_ones = max(
                    maximum_consecutive_ones,
                    current_consecutive_ones
                )
            else:
                current_consecutive_ones = 0

        return maximum_consecutive_ones


# Example usage
solution = Solution()

# Example 1
nums1 = [1,1,0,1,1,1]
print(solution.findMaxConsecutiveOnes(nums1))
# Output: 3

# Example 2
nums2 = [1,0,1,1,0,1]
print(solution.findMaxConsecutiveOnes(nums2))
# Output: 2

# Example 3
nums3 = [1,1,1,1,1]
print(solution.findMaxConsecutiveOnes(nums3))
# Output: 5

# Example 4
nums4 = [0,0,0,0]
print(solution.findMaxConsecutiveOnes(nums4))
# Output: 0

# Example 5
nums5 = [0,1,0,1,1,1,0,1]
print(solution.findMaxConsecutiveOnes(nums5))
# Output: 3

# Example 6
nums6 = [1]
print(solution.findMaxConsecutiveOnes(nums6))
# Output: 1
