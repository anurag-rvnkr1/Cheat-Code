'''
454. 4Sum II

Given four integer arrays nums1, nums2, nums3, and nums4,
return the number of tuples (i, j, k, l) such that:

    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
    Input:
        nums1 = [1,2]
        nums2 = [-2,-1]
        nums3 = [-1,2]
        nums4 = [0,2]

    Output:
        2

Example 2:
    Input:
        nums1 = [0]
        nums2 = [0]
        nums3 = [0]
        nums4 = [0]

    Output:
        1

Constraints:
    1 <= nums1.length == nums2.length == nums3.length == nums4.length <= 200
    -2^28 <= nums[i] <= 2^28
'''

# HashMap + Pair Sums

from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int]
    ) -> int:

        pair_sum_frequency = defaultdict(int)

        # Store sums of nums1 and nums2.
        for number1 in nums1:
            for number2 in nums2:
                pair_sum_frequency[number1 + number2] += 1

        quadruplets = 0

        # Find complementary sums from nums3 and nums4.
        for number3 in nums3:
            for number4 in nums4:
                quadruplets += pair_sum_frequency[-(number3 + number4)]

        return quadruplets


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(solution.fourSumCount(nums1, nums2, nums3, nums4))
# Output: 2

# Example 2
nums5 = [0]
nums6 = [0]
nums7 = [0]
nums8 = [0]

print(solution.fourSumCount(nums5, nums6, nums7, nums8))
# Output: 1

# Example 3
nums9 = [1,-1]
nums10 = [-1,1]
nums11 = [0,2]
nums12 = [0,-2]

print(solution.fourSumCount(nums9, nums10, nums11, nums12))
# Output: 6

# Example 4
nums13 = [2]
nums14 = [-2]
nums15 = [3]
nums16 = [-3]

print(solution.fourSumCount(nums13, nums14, nums15, nums16))
# Output: 1

# Example 5
nums17 = [1,1]
nums18 = [-1,-1]
nums19 = [0]
nums20 = [0]

print(solution.fourSumCount(nums17, nums18, nums19, nums20))
# Output: 4

# Example 6
nums21 = [3,4]
nums22 = [-7,-8]
nums23 = [2,5]
nums24 = [0,1]

print(solution.fourSumCount(nums21, nums22, nums23, nums24))
# Output: 2
