'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is
in the range [1, n] inclusive.

There is only one repeated number in nums, but it may appear more than once.

Return the duplicate number.

You must solve the problem without modifying the array nums and using only
constant extra space.

Example 1:
    Input: nums = [1,3,4,2,2]
    Output: 2

Example 2:
    Input: nums = [3,1,3,4,2]
    Output: 3

Example 3:
    Input: nums = [3,3,3,3,3]
    Output: 3

Constraints:
    1 <= n <= 10^5
    nums.length == n + 1
    1 <= nums[i] <= n
    Only one integer appears two or more times.

Follow-up:
    Can you solve it in O(n) time and O(1) extra space?
'''

# Floyd's Tortoise and Hare Cycle Detection

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the meeting point inside the cycle.
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle.
        tortoise = nums[0]

        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 3, 4, 2, 2]
print(solution.findDuplicate(nums1))
# Output: 2

# Example 2
nums2 = [3, 1, 3, 4, 2]
print(solution.findDuplicate(nums2))
# Output: 3

# Example 3
nums3 = [3, 3, 3, 3, 3]
print(solution.findDuplicate(nums3))
# Output: 3

# Example 4
nums4 = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
print(solution.findDuplicate(nums4))
# Output: 9

# Example 5
nums5 = [1, 1]
print(solution.findDuplicate(nums5))
# Output: 1
