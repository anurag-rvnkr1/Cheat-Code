'''
318. Maximum Product of Word Lengths

Given a string array words, return the maximum value of:

    len(words[i]) * len(words[j])

where the two words do not share any common letters.

If no such pair exists, return 0.

Example 1:
    Input:
        words = ["abcw","baz","foo","bar","xtfn","abcdef"]

    Output:
        16

Explanation:
    "abcw" and "xtfn" share no common letters.

    Product = 4 × 4 = 16

Example 2:
    Input:
        words = ["a","ab","abc","d","cd","bcd","abcd"]

    Output:
        4

Explanation:
    "ab" and "cd"

Example 3:
    Input:
        words = ["a","aa","aaa","aaaa"]

    Output:
        0

Constraints:
    2 <= words.length <= 1000
    1 <= words[i].length <= 1000
    words[i] consists of lowercase English letters.
'''

# Bit Manipulation + String

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        lengths = []

        # Build bitmask for each word.
        for word in words:
            mask = 0

            for character in word:
                mask |= 1 << (ord(character) - ord("a"))

            masks.append(mask)
            lengths.append(len(word))

        maximum_product = 0

        # Compare every pair of words.
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # No common characters.
                if masks[i] & masks[j] == 0:
                    maximum_product = max(
                        maximum_product,
                        lengths[i] * lengths[j]
                    )

        return maximum_product


# Example usage
solution = Solution()

# Example 1
words1 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(solution.maxProduct(words1))
# Output: 16

# Example 2
words2 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
print(solution.maxProduct(words2))
# Output: 4

# Example 3
words3 = ["a", "aa", "aaa", "aaaa"]
print(solution.maxProduct(words3))
# Output: 0

# Example 4
words4 = ["abc", "def", "ghi", "ad"]
print(solution.maxProduct(words4))
# Output: 9

# Example 5
words5 = ["hello", "world", "python", "java"]
print(solution.maxProduct(words5))
# Output: 24

# Example 6
words6 = ["abcd", "efgh", "ijkl", "mnop"]
print(solution.maxProduct(words6))
# Output: 16
