'''
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
    Input: nums = [3,0,1]
    Output: 2

Explanation:
    n = 3
    Numbers are in the range [0,3]
    Missing number is 2.

Example 2:
    Input: nums = [0,1]
    Output: 2

Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8

Constraints:
    n == len(nums)
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All the numbers of nums are unique.

Follow-up:
    Can you implement a solution using O(1) extra space and O(n) runtime?
'''

# Bit Manipulation + Math

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_result = len(nums)

        for index, number in enumerate(nums):
            xor_result ^= index
            xor_result ^= number

        return xor_result


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 0, 1]
print(solution.missingNumber(nums1))
# Output: 2

# Example 2
nums2 = [0, 1]
print(solution.missingNumber(nums2))
# Output: 2

# Example 3
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(solution.missingNumber(nums3))
# Output: 8

# Example 4
nums4 = [0]
print(solution.missingNumber(nums4))
# Output: 1

# Example 5
nums5 = [1]
print(solution.missingNumber(nums5))
# Output: 0
