'''
290. Word Pattern

Given a pattern and a string s, determine if s follows the same pattern.

A string follows a pattern if there is a bijection between a letter in pattern
and a non-empty word in s.

A bijection means:
    - Every pattern character maps to exactly one word.
    - Every word maps to exactly one pattern character.

Example 1:
    Input:
        pattern = "abba"
        s = "dog cat cat dog"

    Output:
        True

Example 2:
    Input:
        pattern = "abba"
        s = "dog cat cat fish"

    Output:
        False

Example 3:
    Input:
        pattern = "aaaa"
        s = "dog cat cat dog"

    Output:
        False

Constraints:
    1 <= pattern.length <= 300
    pattern consists of lowercase English letters.
    1 <= s.length <= 3000
    s contains lowercase English letters and spaces.
    Words in s are separated by a single space.
'''

# HashMap + String


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):

            # Existing character must map to the same word.
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word

            # Existing word must map to the same character.
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char

        return True


# Example usage
solution = Solution()

# Example 1
pattern1 = "abba"
s1 = "dog cat cat dog"
print(solution.wordPattern(pattern1, s1))
# Output: True

# Example 2
pattern2 = "abba"
s2 = "dog cat cat fish"
print(solution.wordPattern(pattern2, s2))
# Output: False

# Example 3
pattern3 = "aaaa"
s3 = "dog cat cat dog"
print(solution.wordPattern(pattern3, s3))
# Output: False

# Example 4
pattern4 = "abba"
s4 = "dog dog dog dog"
print(solution.wordPattern(pattern4, s4))
# Output: False

# Example 5
pattern5 = "abc"
s5 = "one two three"
print(solution.wordPattern(pattern5, s5))
# Output: True

# Example 6
pattern6 = "abc"
s6 = "one two one"
print(solution.wordPattern(pattern6, s6))
# Output: False
