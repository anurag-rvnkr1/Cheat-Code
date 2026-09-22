'''
315. Count of Smaller Numbers After Self

Given an integer array nums, return an integer array counts where counts[i]
is the number of smaller elements to the right of nums[i].

Example 1:
    Input:
        nums = [5,2,6,1]

    Output:
        [2,1,1,0]

Explanation:
    5 -> (2,1)
    2 -> (1)
    6 -> (1)
    1 -> ()

Example 2:
    Input:
        nums = [-1]

    Output:
        [0]

Example 3:
    Input:
        nums = [-1,-1]

    Output:
        [0,0]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
'''

# Fenwick Tree (Binary Indexed Tree) + Coordinate Compression

from typing import List


class FenwickTree:

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Coordinate Compression
        sorted_unique = sorted(set(nums))

        rank = {
            value: index + 1
            for index, value in enumerate(sorted_unique)
        }

        bit = FenwickTree(len(sorted_unique))
        answer = [0] * len(nums)

        # Traverse from right to left.
        for index in range(len(nums) - 1, -1, -1):
            compressed = rank[nums[index]]

            # Count elements strictly smaller.
            answer[index] = bit.query(compressed - 1)

            # Insert current number.
            bit.update(compressed, 1)

        return answer


# Example usage
solution = Solution()

# Example 1
nums1 = [5, 2, 6, 1]
print(solution.countSmaller(nums1))
# Output: [2, 1, 1, 0]

# Example 2
nums2 = [-1]
print(solution.countSmaller(nums2))
# Output: [0]

# Example 3
nums3 = [-1, -1]
print(solution.countSmaller(nums3))
# Output: [0, 0]

# Example 4
nums4 = [3, 2, 2, 6, 1]
print(solution.countSmaller(nums4))
# Output: [3, 1, 1, 1, 0]

# Example 5
nums5 = [1, 9, 7, 8, 5]
print(solution.countSmaller(nums5))
# Output: [0, 3, 1, 1, 0]

# Example 6
nums6 = [10, 9, 8, 7, 6]
print(solution.countSmaller(nums6))
# Output: [4, 3, 2, 1, 0]
