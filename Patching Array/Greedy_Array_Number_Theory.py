'''
330. Patching Array

Given a sorted integer array nums and an integer n, return the minimum number
of patches required so that every number in the range [1, n] can be formed
using the elements of nums and the patches.

You may insert any positive integer anywhere into nums.

Example 1:
    Input:
        nums = [1,3]
        n = 6

    Output:
        1

Explanation:
    Patch 2.

    Numbers representable become:
        1,2,3,4,5,6

Example 2:
    Input:
        nums = [1,5,10]
        n = 20

    Output:
        2

Explanation:
    Patch 2 and 4.

Example 3:
    Input:
        nums = [1,2,2]
        n = 5

    Output:
        0

Constraints:
    1 <= nums.length <= 1000
    nums is sorted in ascending order.
    1 <= nums[i] <= 10^4
    1 <= n <= 2^31 - 1
'''

# Greedy + Coverage Range

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        index = 0

        # Smallest value currently NOT representable.
        miss = 1

        while miss <= n:

            # Extend coverage using nums[index].
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1

            # Patch "miss" itself.
            else:
                miss += miss
                patches += 1

        return patches


# Example usage
solution = Solution()

# Example 1
nums1 = [1, 3]
n1 = 6
print(solution.minPatches(nums1, n1))
# Output: 1

# Example 2
nums2 = [1, 5, 10]
n2 = 20
print(solution.minPatches(nums2, n2))
# Output: 2

# Example 3
nums3 = [1, 2, 2]
n3 = 5
print(solution.minPatches(nums3, n3))
# Output: 0

# Example 4
nums4 = [2]
n4 = 7
print(solution.minPatches(nums4, n4))
# Output: 2
# Patch 1 and 4

# Example 5
nums5 = []
n5 = 8
print(solution.minPatches(nums5, n5))
# Output: 4
# Patch 1,2,4,8

# Example 6
nums6 = [1,2,31,33]
n6 = 2147483647
print(solution.minPatches(nums6, n6))
# Output: 28
