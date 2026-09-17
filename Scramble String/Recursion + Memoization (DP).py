'''
87. Scramble String

We can scramble a string s to get a string t using the following algorithm:

1. If the length of the string is 1, stop.
2. If the length of the string is greater than 1, do the following:
    - Split the string into two non-empty substrings at a random index.
      If the string is s, divide it into x and y where s = x + y.
    - Randomly decide to swap the two substrings or keep them in the same order.
      After this step, s may become x + y or y + x.
    - Apply the same algorithm recursively on each of the two substrings.

Given two strings s1 and s2 of the same length, return True if s2 is a scrambled string of s1. Otherwise, return False.

Example 1:
    Input: s1 = "great", s2 = "rgeat"
    Output: True
    Explanation:
    "great" can be recursively split and scrambled to form "rgeat".

Example 2:
    Input: s1 = "abcde", s2 = "caebd"
    Output: False

Example 3:
    Input: s1 = "a", s2 = "a"
    Output: True

Constraints:
    s1.length == s2.length
    1 <= s1.length <= 30
    s1 and s2 consist of lowercase English letters.
'''

# Recursion + Memoization (DP)
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        n = len(s1)

        @lru_cache(None)
        def dfs(i1, i2, length):

            # Same substring
            if s1[i1:i1 + length] == s2[i2:i2 + length]:
                return True

            # Different character frequencies -> impossible
            if sorted(s1[i1:i1 + length]) != sorted(s2[i2:i2 + length]):
                return False

            # Try every possible split
            for k in range(1, length):

                # Case 1: Don't swap
                if (
                    dfs(i1, i2, k) and
                    dfs(i1 + k, i2 + k, length - k)
                ):
                    return True

                # Case 2: Swap
                if (
                    dfs(i1, i2 + length - k, k) and
                    dfs(i1 + k, i2, length - k)
                ):
                    return True

            return False

        return dfs(0, 0, n)


# Example usage
solution = Solution()

print(solution.isScramble("great", "rgeat"))  # Output: True
print(solution.isScramble("abcde", "caebd"))  # Output: False
print(solution.isScramble("a", "a"))  # Output: True
print(solution.isScramble("abc", "bca"))  # Output: True
