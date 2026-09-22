'''
334. Increasing Triplet Subsequence

Given an integer array nums, return True if there exists a triplet of indices
(i, j, k) such that:

    i < j < k
    nums[i] < nums[j] < nums[k]

Otherwise, return False.

Example 1:
    Input:
        nums = [1,2,3,4,5]

    Output:
        True

Explanation:
    The triplet (1,2,3) exists.

Example 2:
    Input:
        nums = [5,4,3,2,1]

    Output:
        False

Example 3:
    Input:
        nums = [2,1,5,0,4,6]

    Output:
        True

Explanation:
    The triplet (0,4,6) exists.

Constraints:
    1 <= nums.length <= 5 * 10^5
    -2^31 <= nums[i] <= 2^31 - 1

Follow-up:
    Can you solve it in O(n) time and O(1) space?
'''

# Greedy + Array

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for number in nums:

            if number <= first:
                first = number

            elif number <= second:
                second = number

            else:
                # number > second > first
                return True

        return False


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3,4,5]
print(solution.increasingTriplet(nums1))
# Output: True

# Example 2
nums2 = [5,4,3,2,1]
print(solution.increasingTriplet(nums2))
# Output: False

# Example 3
nums3 = [2,1,5,0,4,6]
print(solution.increasingTriplet(nums3))
# Output: True

# Example 4
nums4 = [20,100,10,12,5,13]
print(solution.increasingTriplet(nums4))
# Output: True

# Example 5
nums5 = [2,4,-2,-3]
print(solution.increasingTriplet(nums5))
# Output: False

# Example 6
nums6 = [1,5,0,4,1,3]
print(solution.increasingTriplet(nums6))
# Output: True
