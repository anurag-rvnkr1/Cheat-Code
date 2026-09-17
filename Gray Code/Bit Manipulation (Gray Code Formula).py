'''
89. Gray Code

An n-bit gray code sequence is a sequence of 2^n integers where:

- Every integer is in the inclusive range [0, 2^n - 1].
- The first integer is 0.
- An integer appears no more than once in the sequence.
- The binary representation of every pair of adjacent integers differs by exactly one bit.
- The binary representation of the first and last integers differs by exactly one bit.

Given an integer n, return any valid n-bit gray code sequence.

Example 1:
    Input: n = 2
    Output: [0,1,3,2]
    Explanation:
    The binary representation of [0,1,3,2] is [00,01,11,10].
    Each adjacent pair differs by exactly one bit, including the first and last elements.

Example 2:
    Input: n = 1
    Output: [0,1]

Constraints:
    1 <= n <= 16
'''

# Bit Manipulation (Gray Code Formula)
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:

        return [i ^ (i >> 1) for i in range(1 << n)]


# Example usage
solution = Solution()

print(solution.grayCode(2))  # Output: [0,1,3,2]
print(solution.grayCode(1))  # Output: [0,1]
print(solution.grayCode(3))  # Output: [0,1,3,2,6,7,5,4]
