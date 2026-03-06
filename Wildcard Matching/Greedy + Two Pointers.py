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
#Greedy + Two Pointers
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        i = j = 0
        star = -1
        match = 0
        
        while i < len(s):
            
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            
            else:
                return False
        
        while j < len(p) and p[j] == '*':
            j += 1
        
        return j == len(p)
    
#Example Usage
solution = Solution()
print(solution.isMatch("aa", "a"))  # Output: False
print(solution.isMatch("aa", "*"))  # Output: True