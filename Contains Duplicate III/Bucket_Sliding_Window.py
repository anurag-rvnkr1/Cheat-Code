'''
220. Contains Duplicate III

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

    - i != j
    - abs(i - j) <= indexDiff
    - abs(nums[i] - nums[j]) <= valueDiff

Return True if such a pair exists, otherwise return False.

Example 1:
    Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
    Output: True

Explanation:
    nums[0] == nums[3] and abs(0 - 3) = 3 <= indexDiff.

Example 2:
    Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
    Output: False

Explanation:
    Although duplicate values exist, no valid pair satisfies both conditions.

Example 3:
    Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 1
    Output: True

Constraints:
    2 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    0 <= indexDiff <= 10^5
    0 <= valueDiff <= 10^9
'''

# Bucket Sort + Sliding Window

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self,
        nums: List[int],
        indexDiff: int,
        valueDiff: int
    ) -> bool:

        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        for i, num in enumerate(nums):

            bucket_id = num // bucket_size

            # Adjust bucket for negative numbers.
            if num < 0:
                bucket_id -= 1

            # Same bucket.
            if bucket_id in buckets:
                return True

            # Previous bucket.
            if (
                bucket_id - 1 in buckets and
                abs(num - buckets[bucket_id - 1]) <= valueDiff
            ):
                return True

            # Next bucket.
            if (
                bucket_id + 1 in buckets and
                abs(num - buckets[bucket_id + 1]) <= valueDiff
            ):
                return True

            buckets[bucket_id] = num

            # Maintain sliding window of size indexDiff.
            if i >= indexDiff:
                old_num = nums[i - indexDiff]

                old_bucket = old_num // bucket_size
                if old_num < 0:
                    old_bucket -= 1

                del buckets[old_bucket]

        return False


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
indexDiff1 = 3
valueDiff1 = 0
print(solution.containsNearbyAlmostDuplicate(nums1, indexDiff1, valueDiff1))
# Output: True

# Example 2
nums2 = [1, 5, 9, 1, 5, 9]
indexDiff2 = 2
valueDiff2 = 3
print(solution.containsNearbyAlmostDuplicate(nums2, indexDiff2, valueDiff2))
# Output: False

# Example 3
nums3 = [1, 2, 3, 1]
indexDiff3 = 3
valueDiff3 = 1
print(solution.containsNearbyAlmostDuplicate(nums3, indexDiff3, valueDiff3))
# Output: True

# Example 4
nums4 = [4, 2]
indexDiff4 = 2
valueDiff4 = 1
print(solution.containsNearbyAlmostDuplicate(nums4, indexDiff4, valueDiff4))
# Output: False
