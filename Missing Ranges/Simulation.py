'''
163. Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover every missing number exactly.
Each range should be represented as:

    - "a" if a == b
    - "a->b" if a < b

Example 1:
    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: ["2","4->49","51->74","76->99"]

Example 2:
    Input: nums = [], lower = 1, upper = 1
    Output: ["1"]

Example 3:
    Input: nums = [], lower = -3, upper = -1
    Output: ["-3->-1"]

Constraints:
    0 <= nums.length <= 100
    -2^31 <= lower <= upper <= 2^31 - 1
    nums is sorted in ascending order.
    All values in nums are unique.
'''

# Simulation

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        previous = lower - 1

        # Add upper + 1 as a sentinel value.
        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else upper + 1

            if current - previous >= 2:
                start = previous + 1
                end = current - 1

                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")

            previous = current

        return result


# Example usage
solution = Solution()

# Example 1
nums1 = [0, 1, 3, 50, 75]
print(solution.findMissingRanges(nums1, 0, 99))
# Output: ['2', '4->49', '51->74', '76->99']

# Example 2
nums2 = []
print(solution.findMissingRanges(nums2, 1, 1))
# Output: ['1']

# Example 3
nums3 = []
print(solution.findMissingRanges(nums3, -3, -1))
# Output: ['-3->-1']

# Example 4
nums4 = [1, 2, 3, 4]
print(solution.findMissingRanges(nums4, 1, 4))
# Output: []
