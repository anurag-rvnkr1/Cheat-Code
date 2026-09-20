'''
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3

Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9
'''

# Boyer-Moore Voting Algorithm

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 2, 3]
print(solution.majorityElement(nums1))  # Output: 3

# Example 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(solution.majorityElement(nums2))  # Output: 2

# Example 3
nums3 = [1]
print(solution.majorityElement(nums3))  # Output: 1

# Example 4
nums4 = [6, 5, 5]
print(solution.majorityElement(nums4))  # Output: 5
