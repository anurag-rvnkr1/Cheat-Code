'''
247. Strobogrammatic Number II

Given an integer n, return all strobogrammatic numbers of length n.

A strobogrammatic number is a number that looks the same when rotated
180 degrees (looked at upside down).

Valid rotation pairs are:
    0 ↔ 0
    1 ↔ 1
    6 ↔ 9
    8 ↔ 8
    9 ↔ 6

Return the answer in any order.

Example 1:
    Input: n = 2
    Output: ["11","69","88","96"]

Example 2:
    Input: n = 1
    Output: ["0","1","8"]

Constraints:
    1 <= n <= 14
'''

# Backtracking

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [
            ("0", "0"),
            ("1", "1"),
            ("6", "9"),
            ("8", "8"),
            ("9", "6")
        ]

        def backtrack(length: int, total_length: int) -> List[str]:
            # Base case for even length.
            if length == 0:
                return [""]

            # Base case for odd length.
            if length == 1:
                return ["0", "1", "8"]

            middle_strings = backtrack(length - 2, total_length)
            result = []

            for middle in middle_strings:
                for left, right in pairs:

                    # Avoid leading zeros.
                    if length == total_length and left == "0":
                        continue

                    result.append(left + middle + right)

            return result

        return backtrack(n, n)


# Example usage
solution = Solution()

# Example 1
n1 = 2
print(sorted(solution.findStrobogrammatic(n1)))
# Output: ['11', '69', '88', '96']

# Example 2
n2 = 1
print(sorted(solution.findStrobogrammatic(n2)))
# Output: ['0', '1', '8']

# Example 3
n3 = 3
print(sorted(solution.findStrobogrammatic(n3)))
# Output:
# ['101', '111', '181', '609', '619', '689',
#  '808', '818', '888', '906', '916', '986']

# Example 4
n4 = 4
print(sorted(solution.findStrobogrammatic(n4)))
# Output includes:
# ['1001', '1111', '1691', '1881', '1961', ...]
