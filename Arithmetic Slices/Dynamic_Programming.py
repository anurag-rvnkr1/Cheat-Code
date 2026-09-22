'''
413. Arithmetic Slices

An integer array is called arithmetic if it consists of at least three elements
and the difference between every two consecutive elements is the same.

Return the number of arithmetic subarrays of nums.

Example 1:
    Input:
        nums = [1,2,3,4]

    Output:
        3

Explanation:
        Arithmetic slices:
            [1,2,3]
            [2,3,4]
            [1,2,3,4]

Example 2:
    Input:
        nums = [1]

    Output:
        0

Constraints:
    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
'''

# Dynamic Programming

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total_slices = 0
        current_slices = 0

        for index in range(2, len(nums)):
            if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
                current_slices += 1
                total_slices += current_slices
            else:
                current_slices = 0

        return total_slices


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3,4]
print(solution.numberOfArithmeticSlices(nums1))
# Output: 3

# Example 2
nums2 = [1]
print(solution.numberOfArithmeticSlices(nums2))
# Output: 0

# Example 3
nums3 = [1,3,5,7,9]
print(solution.numberOfArithmeticSlices(nums3))
# Output: 6

# Example 4
nums4 = [7,7,7,7]
print(solution.numberOfArithmeticSlices(nums4))
# Output: 3

# Example 5
nums5 = [3,-1,-5,-9]
print(solution.numberOfArithmeticSlices(nums5))
# Output: 3

# Example 6
nums6 = [1,2,3,8,9,10]
print(solution.numberOfArithmeticSlices(nums6))
# Output: 2
