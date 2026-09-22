'''
411. Minimum Unique Word Abbreviation

A string abbreviation replaces substrings with their lengths.

For example:
    "word" can be abbreviated as:
    ["word","1ord","w1rd","wo1d","wor1","2rd","w2d","wo2",
     "1o1d","1or1","w1r1","1o2","2r1","3d","w3","4"]

Given a target string and a dictionary of strings, return the shortest
abbreviation of the target that does not conflict with any word in the dictionary.

If multiple shortest abbreviations exist, return any one.

Example 1:
    Input:
        target = "apple"
        dictionary = ["blade"]

    Output:
        "a4"

Example 2:
    Input:
        target = "apple"
        dictionary = ["plain","amber","blade"]

    Output:
        "1p3"

Constraints:
    1 <= target.length <= 21
    0 <= dictionary.length <= 1000
    dictionary[i].length == target.length
    target and dictionary[i] consist of lowercase English letters.
'''

# Bitmask + Backtracking

from typing import List


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        length = len(target)

        # Keep only dictionary words with same length.
        words = [
            word for word in dictionary
            if len(word) == length
        ]

        if not words:
            return str(length)

        # Bitmask of differing characters for each word.
        differences = []

        for word in words:
            mask = 0

            for index in range(length):
                if target[index] != word[index]:
                    mask |= 1 << index

            differences.append(mask)

        best_mask = 0
        best_length = float("inf")

        def abbreviation_length(mask: int) -> int:
            size = 0
            skipped = 0

            for index in range(length):
                if mask & (1 << index):
                    if skipped:
                        size += 1
                        skipped = 0
                    size += 1
                else:
                    skipped += 1

            if skipped:
                size += 1

            return size

        def build_abbreviation(mask: int) -> str:
            abbreviation = []
            skipped = 0

            for index in range(length):
                if mask & (1 << index):
                    if skipped:
                        abbreviation.append(str(skipped))
                        skipped = 0
                    abbreviation.append(target[index])
                else:
                    skipped += 1

            if skipped:
                abbreviation.append(str(skipped))

            return "".join(abbreviation)

        def backtrack(index: int, mask: int):
            nonlocal best_mask, best_length

            current_length = abbreviation_length(mask)

            if current_length >= best_length:
                return

            # Valid abbreviation if it differs from every dictionary word.
            valid = True
            for diff in differences:
                if (mask & diff) == 0:
                    valid = False
                    break

            if valid:
                best_mask = mask
                best_length = current_length
                return

            for position in range(index, length):
                backtrack(position + 1, mask | (1 << position))

        backtrack(0, 0)

        return build_abbreviation(best_mask)


# Example usage
solution = Solution()

# Example 1
target1 = "apple"
dictionary1 = ["blade"]
print(solution.minAbbreviation(target1, dictionary1))
# Output: "a4"

# Example 2
target2 = "apple"
dictionary2 = ["plain","amber","blade"]
print(solution.minAbbreviation(target2, dictionary2))
# Output: "1p3"

# Example 3
target3 = "abcdef"
dictionary3 = ["abcgef","abqdef","xbcdef"]
print(solution.minAbbreviation(target3, dictionary3))
# Output: Valid shortest unique abbreviation

# Example 4
target4 = "hello"
dictionary4 = []
print(solution.minAbbreviation(target4, dictionary4))
# Output: "5"

# Example 5
target5 = "aaaaa"
dictionary5 = ["aaaab","baaaa"]
print(solution.minAbbreviation(target5, dictionary5))
# Output: Valid shortest unique abbreviation

# Example 6
target6 = "coding"
dictionary6 = ["coding","roding","coping"]
print(solution.minAbbreviation(target6, dictionary6))
# Output: Valid shortest unique abbreviation
