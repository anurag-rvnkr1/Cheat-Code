'''
471. Encode String with Shortest Length

Given a string s, encode it using the shortest possible length.

Encoding Rule:
    k[encoded_string]

means encoded_string repeated exactly k times.

Return the shortest encoded string.
If encoding does not shorten the string, return the original string.

Example 1:
    Input:
        s = "aaa"

    Output:
        "aaa"

Example 2:
    Input:
        s = "aaaaa"

    Output:
        "5[a]"

Example 3:
    Input:
        s = "aaaaaaaaaa"

    Output:
        "10[a]"

Example 4:
    Input:
        s = "aabcaabcd"

    Output:
        "2[aabc]d"

Example 5:
    Input:
        s = "abbbabbbcabbbabbbc"

    Output:
        "2[2[abbb]c]"

Constraints:
    1 <= s.length <= 150
    s consists of lowercase English letters.
'''

# Dynamic Programming + String Compression


class Solution:
    def encode(self, s: str) -> str:
        n = len(s)

        dp = [[""] * n for _ in range(n)]

        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                substring = s[start:end + 1]
                dp[start][end] = substring

                # No need to encode very short strings.
                if length < 5:
                    continue

                # Split into two encoded parts.
                for mid in range(start, end):
                    left = dp[start][mid]
                    right = dp[mid + 1][end]

                    if len(left + right) < len(dp[start][end]):
                        dp[start][end] = left + right

                # Check repeated pattern.
                doubled = (substring + substring).find(substring, 1)

                if doubled < len(substring):
                    pattern_length = doubled
                    repeat_count = length // pattern_length

                    encoded_pattern = (
                        str(repeat_count)
                        + "["
                        + dp[start][start + pattern_length - 1]
                        + "]"
                    )

                    if len(encoded_pattern) < len(dp[start][end]):
                        dp[start][end] = encoded_pattern

        return dp[0][n - 1]


# Example usage
solution = Solution()

# Example 1
s1 = "aaa"
print(solution.encode(s1))
# Output: "aaa"

# Example 2
s2 = "aaaaa"
print(solution.encode(s2))
# Output: "5[a]"

# Example 3
s3 = "aaaaaaaaaa"
print(solution.encode(s3))
# Output: "10[a]"

# Example 4
s4 = "aabcaabcd"
print(solution.encode(s4))
# Output: "2[aabc]d"

# Example 5
s5 = "abbbabbbcabbbabbbc"
print(solution.encode(s5))
# Output: "2[2[abbb]c]"

# Example 6
s6 = "abcabcabcabcxyzxyzxyz"
print(solution.encode(s6))
# Output: "4[abc]3[xyz]"
