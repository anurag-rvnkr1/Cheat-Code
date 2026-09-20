'''
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string with the words in reverse order concatenated by a single space.

Note:
    - s may contain leading or trailing spaces.
    - There may be multiple spaces between two words.
    - The returned string should only have a single space separating the words.

Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"

Example 2:
    Input: s = "  hello world  "
    Output: "world hello"

Example 3:
    Input: s = "a good   example"
    Output: "example good a"

Constraints:
    1 <= s.length <= 10^4
    s contains English letters, digits, and spaces.
    There is at least one word in s.
'''

# Two Pointers

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        left = 0
        right = len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)


# Example usage
solution = Solution()

# Example 1
s1 = "the sky is blue"
print(solution.reverseWords(s1))  # Output: "blue is sky the"

# Example 2
s2 = "  hello world  "
print(solution.reverseWords(s2))  # Output: "world hello"

# Example 3
s3 = "a good   example"
print(solution.reverseWords(s3))  # Output: "example good a"

# Example 4
s4 = "  Bob    Loves  Alice   "
print(solution.reverseWords(s4))  # Output: "Alice Loves Bob"
