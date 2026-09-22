'''
320. Generalized Abbreviation

A generalized abbreviation replaces consecutive characters in a word
with their count.

Generate all possible generalized abbreviations of a given word.

Return the abbreviations in any order.

Example 1:
    Input:
        word = "word"

    Output:
        [
            "4","3d","2r1","2rd","1o2","1o1d","1or1","1ord",
            "w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"
        ]

Example 2:
    Input:
        word = "a"

    Output:
        ["1","a"]

Constraints:
    1 <= word.length <= 15
    word consists of lowercase English letters.
'''

# Backtracking + DFS

from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []

        def backtrack(index: int, current: str, count: int):
            # Reached the end of the word.
            if index == len(word):
                if count > 0:
                    current += str(count)

                result.append(current)
                return

            # Option 1: Abbreviate current character.
            backtrack(index + 1, current, count + 1)

            # Option 2: Keep current character.
            next_string = current

            if count > 0:
                next_string += str(count)

            next_string += word[index]

            backtrack(index + 1, next_string, 0)

        backtrack(0, "", 0)

        return result


# Example usage
solution = Solution()

# Example 1
word1 = "word"
print(sorted(solution.generateAbbreviations(word1)))
# Output: 16 abbreviations

# Example 2
word2 = "a"
print(sorted(solution.generateAbbreviations(word2)))
# Output: ['1', 'a']

# Example 3
word3 = "ab"
print(sorted(solution.generateAbbreviations(word3)))
# Output:
# ['2', '1b', 'a1', 'ab']

# Example 4
word4 = "cat"
print(sorted(solution.generateAbbreviations(word4)))
# Output:
# ['3','2t','1a1','1at','c2','c1t','ca1','cat']

# Example 5
word5 = "xy"
print(sorted(solution.generateAbbreviations(word5)))
# Output:
# ['2','1y','x1','xy']
