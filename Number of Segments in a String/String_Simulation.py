'''
434. Number of Segments in a String

A segment is defined as a contiguous sequence of non-space characters.

Given a string s, return the number of segments in the string.

Example 1:
    Input:
        s = "Hello, my name is John"

    Output:
        5

Example 2:
    Input:
        s = "Hello"

    Output:
        1

Example 3:
    Input:
        s = "   "

    Output:
        0

Constraints:
    0 <= s.length <= 300
    s consists of English letters, digits, punctuation, and spaces.
'''

# String Traversal / Simulation

class Solution:
    def countSegments(self, s: str) -> int:
        segments = 0

        for index in range(len(s)):
            if (
                s[index] != " " and
                (index == 0 or s[index - 1] == " ")
            ):
                segments += 1

        return segments


# Example usage
solution = Solution()

# Example 1
s1 = "Hello, my name is John"
print(solution.countSegments(s1))
# Output: 5

# Example 2
s2 = "Hello"
print(solution.countSegments(s2))
# Output: 1

# Example 3
s3 = "   "
print(solution.countSegments(s3))
# Output: 0

# Example 4
s4 = "Hello   World"
print(solution.countSegments(s4))
# Output: 2

# Example 5
s5 = "   OpenAI develops AI models   "
print(solution.countSegments(s5))
# Output: 4

# Example 6
s6 = ""
print(solution.countSegments(s6))
# Output: 0
