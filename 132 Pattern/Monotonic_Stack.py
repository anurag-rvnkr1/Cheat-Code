'''
456. 132 Pattern

Given an integer array nums, return True if there exists a 132 pattern.

A 132 pattern is a subsequence nums[i], nums[j], nums[k] such that:

    i < j < k
    nums[i] < nums[k] < nums[j]

Example 1:
    Input:
        nums = [1,2,3,4]

    Output:
        False

Example 2:
    Input:
        nums = [3,1,4,2]

    Output:
        True

Explanation:
        The pattern is (1,4,2).

Example 3:
    Input:
        nums = [-1,3,2,0]

    Output:
        True

Constraints:
    1 <= nums.length <= 2 * 10^5
    -10^9 <= nums[i] <= 10^9
'''

# Monotonic Stack

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float("-inf")

        # Traverse from right to left.
        for number in reversed(nums):
            if number < third:
                return True

            while stack and stack[-1] < number:
                third = stack.pop()

            stack.append(number)

        return False


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3,4]
print(solution.find132pattern(nums1))
# Output: False

# Example 2
nums2 = [3,1,4,2]
print(solution.find132pattern(nums2))
# Output: True

# Example 3
nums3 = [-1,3,2,0]
print(solution.find132pattern(nums3))
# Output: True

# Example 4
nums4 = [1,0,1,-4,-3]
print(solution.find132pattern(nums4))
# Output: False

# Example 5
nums5 = [6,12,3,4,6,11,20]
print(solution.find132pattern(nums5))
# Output: True

# Example 6
nums6 = [9,8,7,6,5]
print(solution.find132pattern(nums6))
# Output: False
