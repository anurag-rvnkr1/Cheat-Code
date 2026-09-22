'''
442. Find All Duplicates in an Array

Given an integer array nums of length n where:

    - 1 <= nums[i] <= n
    - Each integer appears once or twice.

Return an array of all the integers that appear twice.

You must solve the problem without using extra space and in O(n) time.

Example 1:
    Input:
        nums = [4,3,2,7,8,2,3,1]

    Output:
        [2,3]

Example 2:
    Input:
        nums = [1,1,2]

    Output:
        [1]

Example 3:
    Input:
        nums = [1]

    Output:
        []

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= nums.length
    Each element appears once or twice.
'''

# Array + Cyclic Sort (Index Marking)

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for number in nums:
            index = abs(number) - 1

            if nums[index] < 0:
                duplicates.append(index + 1)
            else:
                nums[index] *= -1

        return duplicates


# Example usage
solution = Solution()

# Example 1
nums1 = [4,3,2,7,8,2,3,1]
print(solution.findDuplicates(nums1.copy()))
# Output: [2,3]

# Example 2
nums2 = [1,1,2]
print(solution.findDuplicates(nums2.copy()))
# Output: [1]

# Example 3
nums3 = [1]
print(solution.findDuplicates(nums3.copy()))
# Output: []

# Example 4
nums4 = [2,2]
print(solution.findDuplicates(nums4.copy()))
# Output: [2]

# Example 5
nums5 = [5,4,6,7,9,3,10,9,5,6]
print(solution.findDuplicates(nums5.copy()))
# Output: [5,6,9]

# Example 6
nums6 = [1,2,3,4,5,6,7,8]
print(solution.findDuplicates(nums6.copy()))
# Output: []
