'''
482. License Key Formatting

You are given a license key string s consisting of alphanumeric characters
and dashes ('-').

Reformat the string such that:

    - All letters are uppercase.
    - Remove all existing dashes.
    - Divide the string into groups.
    - The first group may be shorter than k.
    - Every remaining group has exactly k characters.

Return the formatted license key.

Example 1:
    Input:
        s = "5F3Z-2e-9-w"
        k = 4

    Output:
        "5F3Z-2E9W"

Example 2:
    Input:
        s = "2-5g-3-J"
        k = 2

    Output:
        "2-5G-3J"

Constraints:
    1 <= s.length <= 10^5
    s consists of English letters, digits, and '-'.
    1 <= k <= 10^4
'''

# String Simulation


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = []

        # Remove dashes and convert to uppercase.
        for character in s:
            if character != "-":
                cleaned.append(character.upper())

        cleaned_string = "".join(cleaned)

        result = []

        index = len(cleaned_string)

        # Build groups from the end.
        while index > 0:
            start = max(0, index - k)
            result.append(cleaned_string[start:index])
            index -= k

        return "-".join(reversed(result))


# Example usage
solution = Solution()

# Example 1
s1 = "5F3Z-2e-9-w"
k1 = 4
print(solution.licenseKeyFormatting(s1, k1))
# Output: "5F3Z-2E9W"

# Example 2
s2 = "2-5g-3-J"
k2 = 2
print(solution.licenseKeyFormatting(s2, k2))
# Output: "2-5G-3J"

# Example 3
s3 = "---abc-def-ghij---"
k3 = 3
print(solution.licenseKeyFormatting(s3, k3))
# Output: "ABC-DEF-GHI-J"

# Example 4
s4 = "a-a-a-a"
k4 = 1
print(solution.licenseKeyFormatting(s4, k4))
# Output: "A-A-A-A"

# Example 5
s5 = "abcdef123456"
k5 = 4
print(solution.licenseKeyFormatting(s5, k5))
# Output: "ABCD-EF12-3456"

# Example 6
s6 = "----"
k6 = 2
print(solution.licenseKeyFormatting(s6, k6))
# Output: ""
