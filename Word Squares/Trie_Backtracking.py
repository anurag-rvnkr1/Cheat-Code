'''
425. Word Squares

Given a set of unique words where all words have the same length,
return all possible word squares.

A sequence of words forms a valid word square if the kth row and kth column
read exactly the same string.

Example 1:
    Input:
        words = ["area","lead","wall","lady","ball"]

    Output:
        [
            ["wall","area","lead","lady"],
            ["ball","area","lead","lady"]
        ]

Example 2:
    Input:
        words = ["abat","baba","atan","atal"]

    Output:
        [
            ["baba","abat","baba","atan"],
            ["baba","abat","baba","atal"]
        ]

Constraints:
    1 <= words.length <= 1000
    1 <= words[i].length <= 5
    All words have the same length.
    Words consist of lowercase English letters.
    All words are unique.
'''

# Trie + Backtracking

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode()

            node = node.children[character]
            node.words.append(word)

    def search_prefix(self, prefix: str) -> List[str]:
        node = self.root

        for character in prefix:
            if character not in node.children:
                return []

            node = node.children[character]

        return node.words


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        word_length = len(words[0])
        result = []

        def backtrack(square: List[str]) -> None:
            if len(square) == word_length:
                result.append(square[:])
                return

            index = len(square)

            prefix = ""

            for word in square:
                prefix += word[index]

            for candidate in trie.search_prefix(prefix):
                square.append(candidate)
                backtrack(square)
                square.pop()

        for word in words:
            backtrack([word])

        return result


# Example usage
solution = Solution()

# Example 1
words1 = ["area","lead","wall","lady","ball"]
print(solution.wordSquares(words1))
# Output:
# [
#   ["wall","area","lead","lady"],
#   ["ball","area","lead","lady"]
# ]

# Example 2
words2 = ["abat","baba","atan","atal"]
print(solution.wordSquares(words2))
# Output:
# [
#   ["baba","abat","baba","atan"],
#   ["baba","abat","baba","atal"]
# ]

# Example 3
words3 = ["aaaa","aaaa","aaaa","aaaa"]
print(solution.wordSquares(words3))
# Output: All possible valid word squares.

# Example 4
words4 = ["abcd","bnrt","crmy","dtye"]
print(solution.wordSquares(words4))
# Output: [["abcd","bnrt","crmy","dtye"]]

# Example 5
words5 = ["ball","area","lead","lady"]
print(solution.wordSquares(words5))
# Output: [["ball","area","lead","lady"]]

# Example 6
words6 = ["cool","oven","else","lens","ogle"]
print(solution.wordSquares(words6))
# Output: All valid word squares.
