'''
338. Counting Bits

Given an integer n, return an array answer of length n + 1 where
answer[i] is the number of 1's in the binary representation of i.

Example 1:
    Input:
        n = 2

    Output:
        [0,1,1]

Example 2:
    Input:
        n = 5

    Output:
        [0,1,1,2,1,2]

Constraints:
    0 <= n <= 10^5

Follow-up:
    It is very easy to come up with a solution with O(n log n) runtime.
    Can you do it in linear time O(n) and possibly in a single pass?
'''

# Bit Dynamic Programming

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        dp = [0] * (n + 1)

        for number in range(1, n + 1):
            dp[number] = dp[number >> 1] + (number & 1)

        return dp


# Example usage
solution = Solution()

# Example 1
n1 = 2
print(solution.countBits(n1))
# Output: [0,1,1]

# Example 2
n2 = 5
print(solution.countBits(n2))
# Output: [0,1,1,2,1,2]

# Example 3
n3 = 0
print(solution.countBits(n3))
# Output: [0]

# Example 4
n4 = 8
print(solution.countBits(n4))
# Output: [0,1,1,2,1,2,2,3,1]

# Example 5
n5 = 10
print(solution.countBits(n5))
# Output: [0,1,1,2,1,2,2,3,1,2,2]

# Example 6
n6 = 16
print(solution.countBits(n6))
# Output:
# [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]
