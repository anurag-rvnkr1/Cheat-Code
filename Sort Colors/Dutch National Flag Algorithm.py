'''
75. Sort Colors

You are given an array nums with n objects colored red, white, or blue. Sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    Explanation:
    The array has two 0s, two 1s, and two 2s.
    Sorting them in-place places all 0s first, then all 1s, then all 2s.

Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]
    Explanation:
    The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.
'''

# Dutch National Flag Algorithm
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


# Example usage
solution = Solution()

nums1 = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums1)
print(nums1)  # Output: [0,0,1,1,2,2]

nums2 = [2, 0, 1]
solution.sortColors(nums2)
print(nums2)  # Output: [0,1,2]

nums3 = [1, 2, 0, 1, 2, 0]
solution.sortColors(nums3)
print(nums3)  # Output: [0,0,1,1,2,2]
