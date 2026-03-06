'''
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.

Example 3:
    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:
    0 <= s.length, p.length <= 2000
    s contains only lowercase English letters.
    p contains only lowercase English letters, '?' or '*'.
'''
#Dynamic Programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        n, m = len(s), len(p)
        
        dp = [[False]*(m+1) for _ in range(n+1)]
        
        dp[0][0] = True
        
        for j in range(1, m+1):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-1]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        
        return dp[n][m]
    
#Example Usage
solution = Solution()
print(solution.isMatch("aa", "a"))  # Output: False
print(solution.isMatch("aa", "*"))  # Output: True