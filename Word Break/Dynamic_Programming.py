'''
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note:
    The same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: True

Explanation:
    Return True because "leetcode" can be segmented as "leet code".

Example 2:
    Input: s = "applepenapple", wordDict = ["apple","pen"]
    Output: True

Explanation:
    Return True because "applepenapple" can be segmented as
    "apple pen apple".
    Note that you are allowed to reuse a dictionary word.

Example 3:
    Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: False

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of lowercase English letters.
    All the strings of wordDict are unique.
'''

# Dynamic Programming

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        # dp[i] = True if s[:i] can be segmented.
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# Example usage
solution = Solution()

# Example 1
s1 = "leetcode"
wordDict1 = ["leet", "code"]

print(solution.wordBreak(s1, wordDict1))  # Output: True

# Example 2
s2 = "applepenapple"
wordDict2 = ["apple", "pen"]

print(solution.wordBreak(s2, wordDict2))  # Output: True

# Example 3
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]

print(solution.wordBreak(s3, wordDict3))  # Output: False

# Example 4
s4 = "cars"
wordDict4 = ["car", "ca", "rs"]

print(solution.wordBreak(s4, wordDict4))  # Output: True
