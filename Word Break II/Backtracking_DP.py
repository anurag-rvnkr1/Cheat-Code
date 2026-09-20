'''
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word.

Return all such possible sentences in any order.

Note:
    The same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
    Input: s = "catsanddog"
    Output: ["cats and dog","cat sand dog"]

Example 2:
    Input: s = "pineapplepenapple"
    Output: [
        "pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"
    ]

Example 3:
    Input: s = "catsandog"
    Output: []

Constraints:
    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of lowercase English letters.
    All strings in wordDict are unique.
'''

# Backtracking + Dynamic Programming (Memoization)

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    for suffix in dfs(end):
                        if suffix:
                            sentences.append(word + " " + suffix)
                        else:
                            sentences.append(word)

            memo[start] = sentences
            return sentences

        return dfs(0)


# Example usage
solution = Solution()

# Example 1
s1 = "catsanddog"
wordDict1 = ["cat", "cats", "and", "sand", "dog"]

print(solution.wordBreak(s1, wordDict1))
# Output: ['cat sand dog', 'cats and dog']

# Example 2
s2 = "pineapplepenapple"
wordDict2 = ["apple", "pen", "applepen", "pine", "pineapple"]

print(solution.wordBreak(s2, wordDict2))
# Output:
# ['pine apple pen apple',
#  'pine applepen apple',
#  'pineapple pen apple']

# Example 3
s3 = "catsandog"
wordDict3 = ["cats", "dog", "sand", "and", "cat"]

print(solution.wordBreak(s3, wordDict3))
# Output: []
