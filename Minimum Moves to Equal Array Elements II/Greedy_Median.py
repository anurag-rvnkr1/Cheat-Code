'''
462. Minimum Moves to Equal Array Elements II

Given an integer array nums, return the minimum number of moves required to make
all array elements equal.

In one move, you may increment or decrement a single element by 1.

Example 1:
    Input:
        nums = [1,2,3]

    Output:
        2

Explanation:
        Move 1 -> 2
        Move 3 -> 2

Example 2:
    Input:
        nums = [1,10,2,9]

    Output:
        16

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
'''

# Greedy + Median

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        median = nums[len(nums) // 2]

        moves = 0

        for number in nums:
            moves += abs(number - median)

        return moves


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3]
print(solution.minMoves2(nums1))
# Output: 2

# Example 2
nums2 = [1,10,2,9]
print(solution.minMoves2(nums2))
# Output: 16

# Example 3
nums3 = [1]
print(solution.minMoves2(nums3))
# Output: 0

# Example 4
nums4 = [1,0,0,8,6]
print(solution.minMoves2(nums4))
# Output: 14

# Example 5
nums5 = [-5,-2,-1,0,3]
print(solution.minMoves2(nums5))
# Output: 9

# Example 6
nums6 = [100,200,300,400,500]
print(solution.minMoves2(nums6))
# Output: 600
