'''
477. Total Hamming Distance

The Hamming distance between two integers is the number of bit positions
where they differ.

Given an integer array nums, return the total Hamming distance between
all pairs of numbers.

Example 1:
    Input:
        nums = [4,14,2]

    Output:
        6

Explanation:
        Hamming distances:
        (4,14) = 2
        (4,2)  = 2
        (14,2) = 2
        Total = 6

Example 2:
    Input:
        nums = [4,14,4]

    Output:
        4

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
'''

# Bit Manipulation + Greedy Counting

from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)

        # Check every bit position (0 to 30 for nums <= 10^9).
        for bit in range(31):
            ones = 0

            for number in nums:
                if (number >> bit) & 1:
                    ones += 1

            zeros = n - ones

            # Every 1 pairs with every 0.
            total_distance += ones * zeros

        return total_distance


# Example usage
solution = Solution()

# Example 1
nums1 = [4,14,2]
print(solution.totalHammingDistance(nums1))
# Output: 6

# Example 2
nums2 = [4,14,4]
print(solution.totalHammingDistance(nums2))
# Output: 4

# Example 3
nums3 = [1,2,3]
print(solution.totalHammingDistance(nums3))
# Output: 4

# Example 4
nums4 = [0,0,0]
print(solution.totalHammingDistance(nums4))
# Output: 0

# Example 5
nums5 = [1,1,1,1]
print(solution.totalHammingDistance(nums5))
# Output: 0

# Example 6
nums6 = [5,9,15,20]
print(solution.totalHammingDistance(nums6))
# Output: 18
