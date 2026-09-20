'''
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s
which equals t.

A subsequence of a string is a new string generated from the original string
by deleting some (can be none) characters without changing the relative order
of the remaining characters.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
    Input: s = "rabbbit", t = "rabbit"
    Output: 3

Example 2:
    Input: s = "babgbag", t = "bag"
    Output: 5

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
'''

# Dynamic Programming

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] = number of ways t[:j] can be formed from s[:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty string t can always be formed
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


# Example usage
solution = Solution()

# Example 1
print(solution.numDistinct("rabbbit", "rabbit"))  # Output: 3

# Example 2
print(solution.numDistinct("babgbag", "bag"))  # Output: 5

# Example 3
print(solution.numDistinct("abc", "abc"))  # Output: 1

# Example 4
print(solution.numDistinct("abc", "abcd"))  # Output: 0
