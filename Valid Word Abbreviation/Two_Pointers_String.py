'''
408. Valid Word Abbreviation

Given a non-empty string word and an abbreviation abbr, return True if the
abbreviation matches the given word.

Rules:
    - Digits in abbr represent the number of characters skipped in word.
    - Leading zeros are not allowed in numbers.

Example 1:
    Input:
        word = "internationalization"
        abbr = "i12iz4n"

    Output:
        True

Example 2:
    Input:
        word = "apple"
        abbr = "a2e"

    Output:
        False

Constraints:
    1 <= word.length <= 20
    1 <= abbr.length <= 10
    word consists of lowercase English letters.
    abbr consists of lowercase English letters and digits.
'''

# Two Pointers + String Parsing

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_pointer = 0
        abbr_pointer = 0

        while word_pointer < len(word) and abbr_pointer < len(abbr):

            # Character match.
            if abbr[abbr_pointer].isalpha():
                if word[word_pointer] != abbr[abbr_pointer]:
                    return False

                word_pointer += 1
                abbr_pointer += 1

            else:
                # Leading zero is invalid.
                if abbr[abbr_pointer] == "0":
                    return False

                number = 0

                while (
                    abbr_pointer < len(abbr) and
                    abbr[abbr_pointer].isdigit()
                ):
                    number = number * 10 + int(abbr[abbr_pointer])
                    abbr_pointer += 1

                word_pointer += number

        return (
            word_pointer == len(word) and
            abbr_pointer == len(abbr)
        )


# Example usage
solution = Solution()

# Example 1
word1 = "internationalization"
abbr1 = "i12iz4n"
print(solution.validWordAbbreviation(word1, abbr1))
# Output: True

# Example 2
word2 = "apple"
abbr2 = "a2e"
print(solution.validWordAbbreviation(word2, abbr2))
# Output: False

# Example 3
word3 = "substitution"
abbr3 = "s10n"
print(solution.validWordAbbreviation(word3, abbr3))
# Output: True

# Example 4
word4 = "substitution"
abbr4 = "sub4u4"
print(solution.validWordAbbreviation(word4, abbr4))
# Output: True

# Example 5
word5 = "substitution"
abbr5 = "12"
print(solution.validWordAbbreviation(word5, abbr5))
# Output: True

# Example 6
word6 = "substitution"
abbr6 = "s010n"
print(solution.validWordAbbreviation(word6, abbr6))
# Output: False
