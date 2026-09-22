'''
421. Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
where 0 <= i <= j < n.

Example 1:
    Input:
        nums = [3,10,5,25,2,8]

    Output:
        28

Explanation:
        Maximum XOR is 5 XOR 25 = 28.

Example 2:
    Input:
        nums = [0]

    Output:
        0

Example 3:
    Input:
        nums = [2,4]

    Output:
        6

Constraints:
    1 <= nums.length <= 2 * 10^5
    0 <= nums[i] <= 2^31 - 1
'''

# Trie + Bit Manipulation

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        # Insert numbers into the bitwise trie.
        for number in nums:
            current = root

            for bit in range(31, -1, -1):
                value = (number >> bit) & 1

                if value not in current.children:
                    current.children[value] = TrieNode()

                current = current.children[value]

        maximum_xor = 0

        # Find best XOR for every number.
        for number in nums:
            current = root
            current_xor = 0

            for bit in range(31, -1, -1):
                value = (number >> bit) & 1
                opposite = 1 - value

                if opposite in current.children:
                    current_xor |= (1 << bit)
                    current = current.children[opposite]
                else:
                    current = current.children[value]

            maximum_xor = max(maximum_xor, current_xor)

        return maximum_xor


# Example usage
solution = Solution()

# Example 1
nums1 = [3,10,5,25,2,8]
print(solution.findMaximumXOR(nums1))
# Output: 28

# Example 2
nums2 = [0]
print(solution.findMaximumXOR(nums2))
# Output: 0

# Example 3
nums3 = [2,4]
print(solution.findMaximumXOR(nums3))
# Output: 6

# Example 4
nums4 = [8,10,2]
print(solution.findMaximumXOR(nums4))
# Output: 10

# Example 5
nums5 = [14,70,53,83,49,91,36,80,92,51,66,70]
print(solution.findMaximumXOR(nums5))
# Output: 127

# Example 6
nums6 = [1,2,3,4,5]
print(solution.findMaximumXOR(nums6))
# Output: 7
