'''
164. Maximum Gap

Given an integer array nums, return the maximum difference between two successive
elements in its sorted form.

If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
    Input: nums = [3,6,9,1]
    Output: 3

Explanation:
    The sorted form of the array is [1,3,6,9].
    The maximum gap is 3.

Example 2:
    Input: nums = [10]
    Output: 0

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
'''

# Bucket Sort (Pigeonhole Principle)

from typing import List
import math


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        minimum = min(nums)
        maximum = max(nums)

        if minimum == maximum:
            return 0

        # Bucket size and number of buckets.
        bucket_size = max(1, math.ceil((maximum - minimum) / (n - 1)))
        bucket_count = (maximum - minimum) // bucket_size + 1

        bucket_min = [float("inf")] * bucket_count
        bucket_max = [float("-inf")] * bucket_count
        bucket_used = [False] * bucket_count

        # Place numbers into buckets.
        for num in nums:
            index = (num - minimum) // bucket_size

            bucket_min[index] = min(bucket_min[index], num)
            bucket_max[index] = max(bucket_max[index], num)
            bucket_used[index] = True

        max_gap = 0
        previous_max = minimum

        # Calculate maximum gap between consecutive non-empty buckets.
        for i in range(bucket_count):
            if not bucket_used[i]:
                continue

            max_gap = max(max_gap, bucket_min[i] - previous_max)
            previous_max = bucket_max[i]

        return max_gap


# Example usage
solution = Solution()

# Example 1
nums1 = [3, 6, 9, 1]
print(solution.maximumGap(nums1))  # Output: 3

# Example 2
nums2 = [10]
print(solution.maximumGap(nums2))  # Output: 0

# Example 3
nums3 = [1, 10000000]
print(solution.maximumGap(nums3))  # Output: 9999999

# Example 4
nums4 = [1, 1, 1, 1]
print(solution.maximumGap(nums4))  # Output: 0
