'''
219. Contains Duplicate II

Given an integer array nums and an integer k, return True if there are two
distinct indices i and j in the array such that:

    - nums[i] == nums[j]
    - abs(i - j) <= k

Otherwise, return False.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: True

Explanation:
    nums[0] == nums[3] and abs(0 - 3) = 3 <= k.

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: True

Explanation:
    nums[2] == nums[3] and abs(2 - 3) = 1 <= k.

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: False

Explanation:
    Duplicate elements exist, but all are more than k indices apart.

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    0 <= k <= 10^5
'''

# HashMap + Sliding Window

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for index, value in enumerate(nums):
            if value in last_seen and index - last_seen[value] <= k:
                return True

            last_seen[value] = index

        return False


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
k1 = 3
print(solution.containsNearbyDuplicate(nums1, k1))  # Output: True

# Example 2
nums2 = [1, 0, 1, 1]
k2 = 1
print(solution.containsNearbyDuplicate(nums2, k2))  # Output: True

# Example 3
nums3 = [1, 2, 3, 1, 2, 3]
k3 = 2
print(solution.containsNearbyDuplicate(nums3, k3))  # Output: False

# Example 4
nums4 = [99, 99]
k4 = 2
print(solution.containsNearbyDuplicate(nums4, k4))  # Output: True
