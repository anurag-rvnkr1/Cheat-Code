'''
217. Contains Duplicate

Given an integer array nums, return True if any value appears at least twice
in the array, and return False if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: True

Example 2:
    Input: nums = [1,2,3,4]
    Output: False

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: True

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
'''

# Hash Set

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
print(solution.containsDuplicate(nums1))  # Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(solution.containsDuplicate(nums2))  # Output: False

# Example 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(solution.containsDuplicate(nums3))  # Output: True

# Example 4
nums4 = [5]
print(solution.containsDuplicate(nums4))  # Output: False
