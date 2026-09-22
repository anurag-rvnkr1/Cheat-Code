'''
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in the array.

If the third distinct maximum does not exist, return the maximum number.

Example 1:
    Input:
        nums = [3,2,1]

    Output:
        1

Example 2:
    Input:
        nums = [1,2]

    Output:
        2

Example 3:
    Input:
        nums = [2,2,3,1]

    Output:
        1

Constraints:
    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1
'''

# Greedy + Set

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None

        for number in nums:
            if number in (first, second, third):
                continue

            if first is None or number > first:
                third = second
                second = first
                first = number

            elif second is None or number > second:
                third = second
                second = number

            elif third is None or number > third:
                third = number

        return third if third is not None else first


# Example usage
solution = Solution()

# Example 1
nums1 = [3,2,1]
print(solution.thirdMax(nums1))
# Output: 1

# Example 2
nums2 = [1,2]
print(solution.thirdMax(nums2))
# Output: 2

# Example 3
nums3 = [2,2,3,1]
print(solution.thirdMax(nums3))
# Output: 1

# Example 4
nums4 = [5,2,2]
print(solution.thirdMax(nums4))
# Output: 5

# Example 5
nums5 = [1,2,2,5,3,5]
print(solution.thirdMax(nums5))
# Output: 2

# Example 6
nums6 = [10,9,8,7,6]
print(solution.thirdMax(nums6))
# Output: 8
