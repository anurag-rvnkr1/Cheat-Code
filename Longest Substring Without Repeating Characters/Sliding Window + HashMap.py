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
# Sliding Window + HashMap Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        l = 0
        ans = 0

        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                l = last[ch] + 1

            last[ch] = r
            ans = max(ans, r - l + 1)

        return ans

# Example usage:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  
print(solution.lengthOfLongestSubstring("bbbbb"))     
print(solution.lengthOfLongestSubstring("pwwkew"))  