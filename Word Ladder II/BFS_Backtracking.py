'''
126. Word Ladder II

A transformation sequence from beginWord to endWord using a dictionary wordList is a
sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    - Every adjacent pair of words differs by a single letter.
    - Every si is in wordList.
    - sk == endWord.

Return all the shortest transformation sequences from beginWord to endWord.
If no such sequence exists, return an empty list.

Example 1:
    Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
    Output:
        [["hit","hot","dot","dog","cog"],
         ["hit","hot","lot","log","cog"]]

Example 2:
    Input:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
    Output:
        []

Constraints:
    1 <= beginWord.length <= 5
    endWord.length == beginWord.length
    1 <= wordList.length <= 500
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
'''

# Breadth-First Search (BFS) + Backtracking

from typing import List
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            next_level = defaultdict(list)

            for word in level:
                wordSet.discard(word)

            for word in level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in wordSet:
                            next_level[new_word].append(word)

                            if new_word == endWord:
                                found = True

            level = next_level.keys()

            for word in next_level:
                parents[word].extend(next_level[word])

        result = []

        def backtrack(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                backtrack(parent, path + [parent])

        if found:
            backtrack(endWord, [endWord])

        return result


# Example usage
solution = Solution()

# Example 1
beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution.findLadders(beginWord1, endWord1, wordList1))
# Output:
# [['hit', 'hot', 'dot', 'dog', 'cog'],
#  ['hit', 'hot', 'lot', 'log', 'cog']]

# Example 2
beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot", "dot", "dog", "lot", "log"]

print(solution.findLadders(beginWord2, endWord2, wordList2))
# Output: []
