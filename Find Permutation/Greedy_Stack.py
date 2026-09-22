'''
484. Find Permutation

A permutation perm of the first n positive integers satisfies a signature string s
consisting of characters:

    'I' -> Increasing
    'D' -> Decreasing

Return the lexicographically smallest permutation that matches the signature.

Example 1:
    Input:
        s = "I"

    Output:
        [1,2]

Example 2:
    Input:
        s = "DI"

    Output:
        [2,1,3]

Example 3:
    Input:
        s = "DDI"

    Output:
        [3,2,1,4]

Constraints:
    1 <= s.length <= 10^5
    s consists only of 'I' and 'D'.
'''

# Greedy + Stack

from typing import List


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        permutation = []
        stack = []

        for number in range(1, len(s) + 2):
            stack.append(number)

            # Flush stack whenever we see 'I' or reach the end.
            if number == len(s) + 1 or s[number - 1] == "I":
                while stack:
                    permutation.append(stack.pop())

        return permutation


# Example usage
solution = Solution()

# Example 1
s1 = "I"
print(solution.findPermutation(s1))
# Output: [1,2]

# Example 2
s2 = "DI"
print(solution.findPermutation(s2))
# Output: [2,1,3]

# Example 3
s3 = "DDI"
print(solution.findPermutation(s3))
# Output: [3,2,1,4]

# Example 4
s4 = "IIDDD"
print(solution.findPermutation(s4))
# Output: [1,2,6,5,4,3]

# Example 5
s5 = "DIDI"
print(solution.findPermutation(s5))
# Output: [2,1,4,3,5]

# Example 6
s6 = "III"
print(solution.findPermutation(s6))
# Output: [1,2,3,4]
