'''
336. Palindrome Pairs

Given an array of unique strings words, return all pairs of distinct indices
[i, j] such that:

    words[i] + words[j]

forms a palindrome.

Return the answer in any order.

Example 1:
    Input:
        words = ["abcd","dcba","lls","s","sssll"]

    Output:
        [[0,1],[1,0],[3,2],[2,4]]

Example 2:
    Input:
        words = ["bat","tab","cat"]

    Output:
        [[0,1],[1,0]]

Example 3:
    Input:
        words = ["a",""]

    Output:
        [[0,1],[1,0]]

Constraints:
    1 <= words.length <= 5000
    0 <= words[i].length <= 300
    words[i] consists of lowercase English letters.
    All strings are unique.
'''

# HashMap + Palindrome Checking

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        word_index = {
            word: index
            for index, word in enumerate(words)
        }

        result = []

        def is_palindrome(string: str) -> bool:
            return string == string[::-1]

        for index, word in enumerate(words):

            # Try every possible split.
            for split in range(len(word) + 1):

                prefix = word[:split]
                suffix = word[split:]

                # Case 1:
                # Prefix is palindrome.
                # Reverse suffix should exist before current word.
                if is_palindrome(prefix):
                    reverse_suffix = suffix[::-1]

                    if (
                        reverse_suffix in word_index and
                        word_index[reverse_suffix] != index
                    ):
                        result.append([
                            word_index[reverse_suffix],
                            index
                        ])

                # Case 2:
                # Suffix is palindrome.
                # Reverse prefix should exist after current word.
                if split != len(word) and is_palindrome(suffix):
                    reverse_prefix = prefix[::-1]

                    if (
                        reverse_prefix in word_index and
                        word_index[reverse_prefix] != index
                    ):
                        result.append([
                            index,
                            word_index[reverse_prefix]
                        ])

        return result


# Example usage
solution = Solution()

# Example 1
words1 = ["abcd","dcba","lls","s","sssll"]
print(solution.palindromePairs(words1))
# Output: [[1,0],[0,1],[3,2],[2,4]]

# Example 2
words2 = ["bat","tab","cat"]
print(solution.palindromePairs(words2))
# Output: [[1,0],[0,1]]

# Example 3
words3 = ["a",""]
print(solution.palindromePairs(words3))
# Output: [[0,1],[1,0]]

# Example 4
words4 = ["abc","cba","bc"]
print(solution.palindromePairs(words4))
# Output: [[1,0],[0,1]]

# Example 5
words5 = ["race","car","ecar",""]
print(solution.palindromePairs(words5))
# Output: [[2,1],[1,0]]

# Example 6
words6 = ["madam","adam","dam",""]
print(solution.palindromePairs(words6))
# Output: [[0,3],[3,0]]
