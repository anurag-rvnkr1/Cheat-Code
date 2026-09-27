'''
516. Longest Palindromic Subsequence

Given a string s, return the length of the longest palindromic subsequence.

A subsequence is a sequence that can be derived from another sequence by
deleting some characters without changing the order of the remaining characters.

Example 1:
    Input:
        s = "bbbab"

    Output:
        4

Explanation:
        One longest palindromic subsequence is "bbbb".

Example 2:
    Input:
        s = "cbbd"

    Output:
        2

Explanation:
        One longest palindromic subsequence is "bb".

Constraints:
    1 <= s.length <= 1000
    s consists only of lowercase English letters.
'''

# Dynamic Programming (String DP)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # Single characters are palindromes of length 1.
        for i in range(n):
            dp[i][i] = 1

        # Build DP table for increasing substring lengths.
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                if s[left] == s[right]:
                    if length == 2:
                        dp[left][right] = 2
                    else:
                        dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(
                        dp[left + 1][right],
                        dp[left][right - 1]
                    )

        return dp[0][n - 1]


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.longestPalindromeSubseq("bbbab"))
# Output: 4

# Example 2
print(solution.longestPalindromeSubseq("cbbd"))
# Output: 2

# Example 3
print(solution.longestPalindromeSubseq("agbdba"))
# Output: 5

# Example 4
print(solution.longestPalindromeSubseq("abcdef"))
# Output: 1

# Example 5
print(solution.longestPalindromeSubseq("aaaa"))
# Output: 4

# Example 6
print(solution.longestPalindromeSubseq("character"))
# Output: 5
