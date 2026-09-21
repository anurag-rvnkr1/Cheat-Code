'''
229. Majority Element II

Given an integer array nums of size n, find all elements that appear more than
⌊ n/3 ⌋ times.

Return the elements in any order.

Example 1:
    Input: nums = [3,2,3]
    Output: [3]

Example 2:
    Input: nums = [1]
    Output: [1]

Example 3:
    Input: nums = [1,2]
    Output: [1,2]

Constraints:
    1 <= nums.length <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

Follow-up:
    Could you solve the problem in linear time and O(1) extra space?
'''

# Boyer-Moore Voting Algorithm

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        count1 = 0
        count2 = 0

        # Phase 1: Find potential candidates.
        for num in nums:
            if candidate1 == num:
                count1 += 1

            elif candidate2 == num:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Phase 2: Verify the candidates.
        result = []
        count1 = nums.count(candidate1)
        count2 = nums.count(candidate2)

        threshold = len(nums) // 3

        if count1 > threshold:
            result.append(candidate1)

        if candidate2 != candidate1 and count2 > threshold:
            result.append(candidate2)

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 2, 3]
print(solution.majorityElement(nums1))  # Output: [3]

# Example 2
nums2 = [1]
print(solution.majorityElement(nums2))  # Output: [1]

# Example 3
nums3 = [1, 2]
print(solution.majorityElement(nums3))  # Output: [1, 2]

# Example 4
nums4 = [1, 1, 1, 3, 3, 2, 2, 2]
print(solution.majorityElement(nums4))  # Output: [1, 2]
