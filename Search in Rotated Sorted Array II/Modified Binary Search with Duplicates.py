'''
81. Search in Rotated Sorted Array II

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not.

You must decrease the overall operation steps as much as possible.

Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: True

Example 2:
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: False

Constraints:
    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums is guaranteed to be rotated at some pivot.
    -10^4 <= target <= 10^4
'''

# Modified Binary Search with Duplicates
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Cannot determine which half is sorted due to duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


# Example usage
solution = Solution()

print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))  # Output: True
print(solution.search([2, 5, 6, 0, 0, 1, 2], 3))  # Output: False
print(solution.search([1, 1, 1, 3, 1], 3))  # Output: True
print(solution.search([1, 0, 1, 1, 1], 0))  # Output: True
