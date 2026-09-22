'''
448. Find All Numbers Disappeared in an Array

Given an integer array nums of length n where:

    - 1 <= nums[i] <= n
    - Some elements appear twice and others appear once.

Return all the numbers in the range [1, n] that do not appear in nums.

The solution must run in O(n) time and use constant extra space
(excluding the returned list).

Example 1:
    Input:
        nums = [4,3,2,7,8,2,3,1]

    Output:
        [5,6]

Example 2:
    Input:
        nums = [1,1]

    Output:
        [2]

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= nums.length
'''

# Array + Cyclic Sort (Index Marking)

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark visited indices by negating the value.
        for number in nums:
            index = abs(number) - 1

            if nums[index] > 0:
                nums[index] *= -1

        missing_numbers = []

        for index in range(len(nums)):
            if nums[index] > 0:
                missing_numbers.append(index + 1)

        return missing_numbers


# Example usage
solution = Solution()

# Example 1
nums1 = [4,3,2,7,8,2,3,1]
print(solution.findDisappearedNumbers(nums1.copy()))
# Output: [5,6]

# Example 2
nums2 = [1,1]
print(solution.findDisappearedNumbers(nums2.copy()))
# Output: [2]

# Example 3
nums3 = [2,2]
print(solution.findDisappearedNumbers(nums3.copy()))
# Output: [1]

# Example 4
nums4 = [1,2,3,4,5]
print(solution.findDisappearedNumbers(nums4.copy()))
# Output: []

# Example 5
nums5 = [5,4,6,7,9,3,10,9,5,6]
print(solution.findDisappearedNumbers(nums5.copy()))
# Output: [1,2,8]

# Example 6
nums6 = [2,3,2,1,5,6,6,8]
print(solution.findDisappearedNumbers(nums6.copy()))
# Output: [4,7]
