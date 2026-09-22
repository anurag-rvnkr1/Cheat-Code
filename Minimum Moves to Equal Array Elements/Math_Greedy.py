'''
453. Minimum Moves to Equal Array Elements

Given an integer array nums of size n, return the minimum number of moves
required to make all array elements equal.

In one move, you may increment n - 1 elements by 1.

Example 1:
    Input:
        nums = [1,2,3]

    Output:
        3

Explanation:
        [1,2,3] -> [2,3,3]
        [2,3,3] -> [3,4,3]
        [3,4,3] -> [4,4,4]

Example 2:
    Input:
        nums = [1,1,1]

    Output:
        0

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
'''

# Math + Greedy

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum_value = min(nums)

        moves = 0

        for number in nums:
            moves += number - minimum_value

        return moves


# Example usage
solution = Solution()

# Example 1
nums1 = [1,2,3]
print(solution.minMoves(nums1))
# Output: 3

# Example 2
nums2 = [1,1,1]
print(solution.minMoves(nums2))
# Output: 0

# Example 3
nums3 = [5,6,8,8]
print(solution.minMoves(nums3))
# Output: 7

# Example 4
nums4 = [10]
print(solution.minMoves(nums4))
# Output: 0

# Example 5
nums5 = [-1,0,1]
print(solution.minMoves(nums5))
# Output: 3

# Example 6
nums6 = [100,200,300,400]
print(solution.minMoves(nums6))
# Output: 600
