'''
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.

Example 1:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

Explanation:
    Rotate 1 step  -> [7,1,2,3,4,5,6]
    Rotate 2 steps -> [6,7,1,2,3,4,5]
    Rotate 3 steps -> [5,6,7,1,2,3,4]

Example 2:
    Input: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]

Constraints:
    1 <= nums.length <= 10^5
    -2^31 <= nums[i] <= 2^31 - 1
    0 <= k <= 10^5
'''

# Array Reversal

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        # Helper function to reverse elements in-place.
        def reverse(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire array.
        reverse(0, n - 1)

        # Step 2: Reverse the first k elements.
        reverse(0, k - 1)

        # Step 3: Reverse the remaining elements.
        reverse(k, n - 1)


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

# Example 2
nums2 = [-1, -100, 3, 99]
solution.rotate(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]

# Example 3
nums3 = [1, 2]
solution.rotate(nums3, 3)
print(nums3)  # Output: [2, 1]

# Example 4
nums4 = [1]
solution.rotate(nums4, 0)
print(nums4)  # Output: [1]
