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

# Brute Force Approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):
            for j in range(i+1, n+1):
                sub = s[i:j]
                if sub == sub[::-1] and len(sub) > len(ans):
                    ans = sub

        return ans
    
# Example usage:
sol = Solution()
print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba 
print(sol.longestPalindrome("cbbd"))   # Output: "bb"