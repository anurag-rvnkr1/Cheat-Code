'''
291. Word Pattern II

Given a pattern and a string s, return True if s follows the same pattern.

A string follows a pattern if there is a bijection between a letter in pattern
and a non-empty substring in s.

A bijection means:
    - Every pattern character maps to exactly one substring.
    - Every substring maps to exactly one pattern character.

Example 1:
    Input:
        pattern = "abab"
        s = "redblueredblue"

    Output:
        True

Explanation:
    a -> "red"
    b -> "blue"

Example 2:
    Input:
        pattern = "aaaa"
        s = "asdasdasdasd"

    Output:
        True

Explanation:
    a -> "asd"

Example 3:
    Input:
        pattern = "aabb"
        s = "xyzabcxzyabc"

    Output:
        False

Constraints:
    1 <= pattern.length <= 20
    1 <= s.length <= 20
    pattern consists of lowercase English letters.
    s consists of lowercase English letters.
'''

# Backtracking + HashMap


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        used_words = set()

        def backtrack(pattern_index: int, string_index: int) -> bool:
            # Successfully matched both pattern and string.
            if pattern_index == len(pattern) and string_index == len(s):
                return True

            # One finished before the other.
            if pattern_index == len(pattern) or string_index == len(s):
                return False

            current_char = pattern[pattern_index]

            # Existing mapping.
            if current_char in char_to_word:
                mapped_word = char_to_word[current_char]

                if not s.startswith(mapped_word, string_index):
                    return False

                return backtrack(
                    pattern_index + 1,
                    string_index + len(mapped_word)
                )

            # Try every possible substring.
            for end in range(string_index + 1, len(s) + 1):
                candidate = s[string_index:end]

                if candidate in used_words:
                    continue

                char_to_word[current_char] = candidate
                used_words.add(candidate)

                if backtrack(pattern_index + 1, end):
                    return True

                # Backtrack.
                del char_to_word[current_char]
                used_words.remove(candidate)

            return False

        return backtrack(0, 0)


# Example usage
solution = Solution()

# Example 1
pattern1 = "abab"
s1 = "redblueredblue"
print(solution.wordPatternMatch(pattern1, s1))
# Output: True

# Example 2
pattern2 = "aaaa"
s2 = "asdasdasdasd"
print(solution.wordPatternMatch(pattern2, s2))
# Output: True

# Example 3
pattern3 = "aabb"
s3 = "xyzabcxzyabc"
print(solution.wordPatternMatch(pattern3, s3))
# Output: False

# Example 4
pattern4 = "ab"
s4 = "aa"
print(solution.wordPatternMatch(pattern4, s4))
# Output: False

# Example 5
pattern5 = "abc"
s5 = "onetwothree"
print(solution.wordPatternMatch(pattern5, s5))
# Output: True
