'''
422. Valid Word Square

Given an array of strings words, return True if it forms a valid word square.

A sequence of strings forms a valid word square if the kth row and kth column
read exactly the same string for every valid index k.

Example 1:
    Input:
        words = [
            "abcd",
            "bnrt",
            "crmy",
            "dtye"
        ]

    Output:
        True

Example 2:
    Input:
        words = [
            "abcd",
            "bnrt",
            "crm",
            "dt"
        ]

    Output:
        True

Example 3:
    Input:
        words = [
            "ball",
            "area",
            "read",
            "lady"
        ]

    Output:
        False

Constraints:
    1 <= words.length <= 500
    1 <= words[i].length <= 500
    words[i] consists of lowercase English letters.
'''

# Matrix + String Traversal

from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        total_rows = len(words)

        for row in range(total_rows):
            for col in range(len(words[row])):

                # Column index must exist as a row.
                if col >= total_rows:
                    return False

                # Row index must exist in the column string.
                if row >= len(words[col]):
                    return False

                if words[row][col] != words[col][row]:
                    return False

        return True


# Example usage
solution = Solution()

# Example 1
words1 = [
    "abcd",
    "bnrt",
    "crmy",
    "dtye"
]
print(solution.validWordSquare(words1))
# Output: True

# Example 2
words2 = [
    "abcd",
    "bnrt",
    "crm",
    "dt"
]
print(solution.validWordSquare(words2))
# Output: True

# Example 3
words3 = [
    "ball",
    "area",
    "read",
    "lady"
]
print(solution.validWordSquare(words3))
# Output: False

# Example 4
words4 = [
    "abc",
    "b",
    "c"
]
print(solution.validWordSquare(words4))
# Output: True

# Example 5
words5 = [
    "aa",
    "aa"
]
print(solution.validWordSquare(words5))
# Output: True

# Example 6
words6 = [
    "abc",
    "ba"
]
print(solution.validWordSquare(words6))
# Output: False
