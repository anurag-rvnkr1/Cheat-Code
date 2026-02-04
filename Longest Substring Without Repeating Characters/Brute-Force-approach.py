"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 
Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""
# Brute-Force Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            for j in range(i+1, n+1):
                sub = s[i:j]
                if len(set(sub)) == len(sub):
                    ans = max(ans, j-i)
        return ans
    
# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  
print(solution.lengthOfLongestSubstring("bbbbb"))     
print(solution.lengthOfLongestSubstring("pwwkew"))    