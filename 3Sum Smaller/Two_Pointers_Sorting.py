'''
259. 3Sum Smaller

Given an integer array nums and an integer target, return the number of index
triplets (i, j, k) such that:

    0 <= i < j < k < nums.length

and

    nums[i] + nums[j] + nums[k] < target.

Example 1:
    Input: nums = [-2,0,1,3], target = 2
    Output: 2

Explanation:
    The valid triplets are:
    [-2,0,1]
    [-2,0,3]

Example 2:
    Input: nums = [], target = 0
    Output: 0

Example 3:
    Input: nums = [0], target = 0
    Output: 0

Constraints:
    0 <= nums.length <= 3500
    -100 <= nums[i] <= 100
    -100 <= target <= 100
'''

# Two Pointers + Sorting

from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum < target:
                    # All elements between left and right are valid.
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count


# Example usage
solution = Solution()

# Example 1
nums1 = [-2, 0, 1, 3]
target1 = 2
print(solution.threeSumSmaller(nums1, target1))
# Output: 2

# Example 2
nums2 = []
target2 = 0
print(solution.threeSumSmaller(nums2, target2))
# Output: 0

# Example 3
nums3 = [0]
target3 = 0
print(solution.threeSumSmaller(nums3, target3))
# Output: 0

# Example 4
nums4 = [3, 1, 0, -2]
target4 = 4
print(solution.threeSumSmaller(nums4, target4))
# Output: 3
