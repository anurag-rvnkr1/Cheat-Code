'''
214. Shortest Palindrome

You are given a string s. You can convert s to a palindrome by adding characters
in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:
    Input: s = "aacecaaa"
    Output: "aaacecaaa"

Explanation:
    Add one 'a' to the front.

Example 2:
    Input: s = "abcd"
    Output: "dcbabcd"

Explanation:
    Add "dcb" in front of "abcd".

Constraints:
    0 <= s.length <= 5 * 10^4
    s consists of lowercase English letters only.
'''

# KMP (Longest Prefix Suffix)


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        reversed_string = s[::-1]
        combined = s + "#" + reversed_string

        # Build LPS (Longest Prefix Suffix) array.
        lps = [0] * len(combined)
        length = 0

        for i in range(1, len(combined)):
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]

            if combined[i] == combined[length]:
                length += 1
                lps[i] = length

        longest_palindrome_prefix = lps[-1]

        # Add the remaining suffix (reversed) to the front.
        suffix = s[longest_palindrome_prefix:]
        return suffix[::-1] + s


# Example usage
solution = Solution()

# Example 1
s1 = "aacecaaa"
print(solution.shortestPalindrome(s1))
# Output: aaacecaaa

# Example 2
s2 = "abcd"
print(solution.shortestPalindrome(s2))
# Output: dcbabcd

# Example 3
s3 = "aba"
print(solution.shortestPalindrome(s3))
# Output: aba

# Example 4
s4 = "abb"
print(solution.shortestPalindrome(s4))
# Output: bbabb
