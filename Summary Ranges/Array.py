'''
228. Summary Ranges

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.

Each range should be formatted as:
    - "a->b" if a != b
    - "a" if a == b

Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]

Explanation:
    The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]

Constraints:
    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All values of nums are unique.
    nums is sorted in ascending order.
'''

# Array

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums) + 1):

            # End of current consecutive range.
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]

                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{end}")

                # Start a new range if elements remain.
                if i < len(nums):
                    start = nums[i]

        return ranges


# Example usage
solution = Solution()

# Example 1
nums1 = [0, 1, 2, 4, 5, 7]
print(solution.summaryRanges(nums1))
# Output: ['0->2', '4->5', '7']

# Example 2
nums2 = [0, 2, 3, 4, 6, 8, 9]
print(solution.summaryRanges(nums2))
# Output: ['0', '2->4', '6', '8->9']

# Example 3
nums3 = []
print(solution.summaryRanges(nums3))
# Output: []

# Example 4
nums4 = [-3, -2, -1, 1, 2, 4]
print(solution.summaryRanges(nums4))
# Output: ['-3->-1', '1->2', '4']
