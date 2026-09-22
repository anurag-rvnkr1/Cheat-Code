'''
472. Concatenated Words

Given an array of unique strings words, return all concatenated words.

A concatenated word is formed entirely by concatenating at least two shorter
words from the same array.

Example 1:
    Input:
        words = [
            "cat","cats","catsdogcats","dog",
            "dogcatsdog","hippopotamuses",
            "rat","ratcatdogcat"
        ]

    Output:
        [
            "catsdogcats",
            "dogcatsdog",
            "ratcatdogcat"
        ]

Example 2:
    Input:
        words = ["cat","dog","catdog"]

    Output:
        ["catdog"]

Constraints:
    1 <= words.length <= 10^4
    1 <= words[i].length <= 30
    words[i] consists of lowercase English letters.
    All strings are unique.
'''

# Trie + Dynamic Programming

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.is_word = True

    def search(self, word: str, index: int, count: int) -> bool:
        current = self.root

        for position in range(index, len(word)):
            character = word[position]

            if character not in current.children:
                return False

            current = current.children[character]

            if current.is_word:
                if position == len(word) - 1:
                    return count >= 1

                if self.search(word, position + 1, count + 1):
                    return True

        return False


class Solution:
    def findAllConcatenatedWordsInADict(
        self,
        words: List[str]
    ) -> List[str]:

        trie = Trie()

        words.sort(key=len)

        answer = []

        for word in words:
            if word == "":
                continue

            if trie.search(word, 0, 0):
                answer.append(word)

            trie.insert(word)

        return answer


# Example usage
solution = Solution()

# Example 1
words1 = [
    "cat",
    "cats",
    "catsdogcats",
    "dog",
    "dogcatsdog",
    "hippopotamuses",
    "rat",
    "ratcatdogcat"
]

print(solution.findAllConcatenatedWordsInADict(words1))
# Output:
# ['catsdogcats','dogcatsdog','ratcatdogcat']

# Example 2
words2 = ["cat","dog","catdog"]
print(solution.findAllConcatenatedWordsInADict(words2))
# Output: ['catdog']

# Example 3
words3 = ["a","aa","aaa","aaaa","aaaaaa"]
print(solution.findAllConcatenatedWordsInADict(words3))
# Output: ['aa','aaa','aaaa','aaaaaa']

# Example 4
words4 = ["hello","world","helloworld","python","helloworldpython"]
print(solution.findAllConcatenatedWordsInADict(words4))
# Output: ['helloworld','helloworldpython']

# Example 5
words5 = ["ab","abc","cd","abcd","abcabcd"]
print(solution.findAllConcatenatedWordsInADict(words5))
# Output: ['abcd','abcabcd']

# Example 6
words6 = ["rat","cat","dog","ratcat","catdog","ratcatdog"]
print(solution.findAllConcatenatedWordsInADict(words6))
# Output: ['ratcat','catdog','ratcatdog']
