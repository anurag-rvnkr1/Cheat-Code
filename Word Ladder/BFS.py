'''
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    - Every adjacent pair of words differs by a single letter.
    - Every si is in wordList.
    - sk == endWord.

Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from
beginWord to endWord, or 0 if no such sequence exists.

Example 1:
    Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5

    Explanation:
        One shortest transformation sequence is
        "hit" -> "hot" -> "dot" -> "dog" -> "cog".

Example 2:
    Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
    Output: 0

Constraints:
    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
'''

# Breadth-First Search (BFS)

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]

                    if new_word in wordSet:
                        queue.append((new_word, steps + 1))
                        wordSet.remove(new_word)

        return 0


# Example usage
solution = Solution()

# Example 1
beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution.ladderLength(beginWord1, endWord1, wordList1))
# Output: 5

# Example 2
beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot", "dot", "dog", "lot", "log"]

print(solution.ladderLength(beginWord2, endWord2, wordList2))
# Output: 0

# Example 3
beginWord3 = "a"
endWord3 = "c"
wordList3 = ["a", "b", "c"]

print(solution.ladderLength(beginWord3, endWord3, wordList3))
# Output: 2
