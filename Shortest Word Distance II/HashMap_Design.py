'''
244. Shortest Word Distance II

Design a data structure that will be initialized with a list of strings and
can answer shortest distance queries between two different words efficiently.

Implement the WordDistance class:

    - WordDistance(wordsDict) Initializes the object with the array wordsDict.
    - shortest(word1, word2) Returns the shortest distance between word1 and word2.

Example 1:
    Input:
        wordsDict = ["practice","makes","perfect","coding","makes"]

        shortest("coding", "practice")
        shortest("makes", "coding")

    Output:
        3
        1

Explanation:
    WordDistance wordDistance = WordDistance(wordsDict);

    wordDistance.shortest("coding", "practice"); // 3
    wordDistance.shortest("makes", "coding");    // 1

Constraints:
    1 <= wordsDict.length <= 3 * 10^4
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
    word1 != word2
    At most 5000 calls will be made to shortest().
'''

# HashMap + Two Pointers

from typing import List


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_positions = {}

        # Store all indices for every word.
        for index, word in enumerate(wordsDict):
            if word not in self.word_positions:
                self.word_positions[word] = []

            self.word_positions[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        positions1 = self.word_positions[word1]
        positions2 = self.word_positions[word2]

        pointer1 = 0
        pointer2 = 0
        minimum_distance = float("inf")

        # Two-pointer traversal on sorted index lists.
        while pointer1 < len(positions1) and pointer2 < len(positions2):

            minimum_distance = min(
                minimum_distance,
                abs(positions1[pointer1] - positions2[pointer2])
            )

            if positions1[pointer1] < positions2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1

        return minimum_distance


# Example usage
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]

wordDistance = WordDistance(wordsDict)

# Example 1
print(wordDistance.shortest("coding", "practice"))
# Output: 3

# Example 2
print(wordDistance.shortest("makes", "coding"))
# Output: 1

# Example 3
print(wordDistance.shortest("practice", "perfect"))
# Output: 2

# Example 4
print(wordDistance.shortest("makes", "practice"))
# Output: 1
