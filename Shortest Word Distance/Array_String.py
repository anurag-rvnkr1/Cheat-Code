'''
243. Shortest Word Distance

Given an array of strings wordsDict and two different strings word1 and word2,
return the shortest distance between these two words in the list.

Example 1:
    Input:
        wordsDict = ["practice","makes","perfect","coding","makes"]
        word1 = "coding"
        word2 = "practice"

    Output: 3

Explanation:
    "coding" is at index 3 and "practice" is at index 0.
    Distance = |3 - 0| = 3.

Example 2:
    Input:
        wordsDict = ["practice","makes","perfect","coding","makes"]
        word1 = "makes"
        word2 = "coding"

    Output: 1

Explanation:
    "makes" appears at indices 1 and 4.
    The shortest distance to "coding" (index 3) is 1.

Constraints:
    1 <= wordsDict.length <= 3 * 10^4
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
    word1 != word2
'''

# Array + String

from typing import List


class Solution:
    def shortestDistance(
        self,
        wordsDict: List[str],
        word1: str,
        word2: str
    ) -> int:

        index1 = -1
        index2 = -1
        minimum_distance = float("inf")

        for index, word in enumerate(wordsDict):

            if word == word1:
                index1 = index

            elif word == word2:
                index2 = index

            if index1 != -1 and index2 != -1:
                minimum_distance = min(
                    minimum_distance,
                    abs(index1 - index2)
                )

        return minimum_distance


# Example usage
solution = Solution()

# Example 1
wordsDict1 = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"

print(solution.shortestDistance(wordsDict1, word1, word2))
# Output: 3

# Example 2
wordsDict2 = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

print(solution.shortestDistance(wordsDict2, word1, word2))
# Output: 1

# Example 3
wordsDict3 = ["a", "c", "b", "a"]
word1 = "a"
word2 = "b"

print(solution.shortestDistance(wordsDict3, word1, word2))
# Output: 1

# Example 4
wordsDict4 = ["one", "two", "three", "four", "five"]
word1 = "one"
word2 = "five"

print(solution.shortestDistance(wordsDict4, word1, word2))
# Output: 4
