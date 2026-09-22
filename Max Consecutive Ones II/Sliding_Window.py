'''
487. Max Consecutive Ones II

Given a binary array nums, return the maximum number of consecutive 1's
if you can flip at most one 0.

Example 1:
    Input:
        nums = [1,0,1,1,0]

    Output:
        4

Explanation:
        Flip the first 0 to get [1,1,1,1,0].

Example 2:
    Input:
        nums = [1,0,1,1,0,1]

    Output:
        4

Constraints:
    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
'''

# Sliding Window

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        maximum_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1

                left += 1

            maximum_length = max(
                maximum_length,
                right - left + 1
            )

        return maximum_length


# Example usage
solution = Solution()

# Example 1
nums1 = [1,0,1,1,0]
print(solution.findMaxConsecutiveOnes(nums1))
# Output: 4

# Example 2
nums2 = [1,0,1,1,0,1]
print(solution.findMaxConsecutiveOnes(nums2))
# Output: 4

# Example 3
nums3 = [1,1,1,1]
print(solution.findMaxConsecutiveOnes(nums3))
# Output: 4

# Example 4
nums4 = [0,0,0]
print(solution.findMaxConsecutiveOnes(nums4))
# Output: 1

# Example 5
nums5 = [1,0,0,1,1,1]
print(solution.findMaxConsecutiveOnes(nums5))
# Output: 4

# Example 6
nums6 = [0,1,1,1,0,1,1]
print(solution.findMaxConsecutiveOnes(nums6))
# Output: 6
