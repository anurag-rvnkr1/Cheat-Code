'''
245. Shortest Word Distance III

Given an array of strings wordsDict and two strings word1 and word2,
return the shortest distance between these two words in the list.

Unlike Shortest Word Distance I, word1 and word2 may be the same.

Example 1:
    Input:
        wordsDict = ["practice","makes","perfect","coding","makes"]
        word1 = "makes"
        word2 = "coding"

    Output: 1

Example 2:
    Input:
        wordsDict = ["practice","makes","perfect","coding","makes"]
        word1 = "makes"
        word2 = "makes"

    Output: 3

Explanation:
    "makes" appears at indices 1 and 4.
    Distance = |4 - 1| = 3.

Constraints:
    1 <= wordsDict.length <= 10^5
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
'''

# Array + String

from typing import List


class Solution:
    def shortestWordDistance(
        self,
        wordsDict: List[str],
        word1: str,
        word2: str
    ) -> int:

        minimum_distance = float("inf")

        if word1 == word2:
            previous_index = -1

            for index, word in enumerate(wordsDict):
                if word == word1:
                    if previous_index != -1:
                        minimum_distance = min(
                            minimum_distance,
                            index - previous_index
                        )

                    previous_index = index

        else:
            index1 = -1
            index2 = -1

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
word1 = "makes"
word2 = "coding"

print(solution.shortestWordDistance(wordsDict1, word1, word2))
# Output: 1

# Example 2
wordsDict2 = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"

print(solution.shortestWordDistance(wordsDict2, word1, word2))
# Output: 3

# Example 3
wordsDict3 = ["a", "b", "a", "c", "a"]
word1 = "a"
word2 = "a"

print(solution.shortestWordDistance(wordsDict3, word1, word2))
# Output: 2

# Example 4
wordsDict4 = ["one", "two", "three", "two", "one"]
word1 = "one"
word2 = "two"

print(solution.shortestWordDistance(wordsDict4, word1, word2))
# Output: 1
