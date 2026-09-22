'''
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking one substring
and repeating it multiple times.

Return True if possible, otherwise False.

Example 1:
    Input:
        s = "abab"

    Output:
        True

Explanation:
        "ab" repeated twice.

Example 2:
    Input:
        s = "aba"

    Output:
        False

Example 3:
    Input:
        s = "abcabcabcabc"

    Output:
        True

Explanation:
        "abc" repeated four times.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
'''

# String + KMP (LPS Array)


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        # Build LPS (Longest Prefix Suffix) array.
        lps = [0] * n

        length = 0
        index = 1

        while index < n:
            if s[index] == s[length]:
                length += 1
                lps[index] = length
                index += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[index] = 0
                index += 1

        longest_prefix_suffix = lps[-1]

        return (
            longest_prefix_suffix > 0 and
            n % (n - longest_prefix_suffix) == 0
        )


# Example usage
solution = Solution()

# Example 1
s1 = "abab"
print(solution.repeatedSubstringPattern(s1))
# Output: True

# Example 2
s2 = "aba"
print(solution.repeatedSubstringPattern(s2))
# Output: False

# Example 3
s3 = "abcabcabcabc"
print(solution.repeatedSubstringPattern(s3))
# Output: True

# Example 4
s4 = "aaaa"
print(solution.repeatedSubstringPattern(s4))
# Output: True

# Example 5
s5 = "a"
print(solution.repeatedSubstringPattern(s5))
# Output: False

# Example 6
s6 = "xyzxyzxyz"
print(solution.repeatedSubstringPattern(s6))
# Output: True
