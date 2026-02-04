""" 
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"
 

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
"""

# Expand Around Center Approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            p1 = expand(i, i)     # odd
            p2 = expand(i, i+1)   # even

            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2

        return res
# Example usage:
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba
print(sol.longestPalindrome("cbbd"))   # Output: "bb"