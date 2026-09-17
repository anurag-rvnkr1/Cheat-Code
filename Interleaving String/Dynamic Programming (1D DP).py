'''
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where:
- s = s1 + s2 + ... + sn
- t = t1 + t2 + ... + tm
- |n - m| <= 1
- The interleaving is:
    s1 + t1 + s2 + t2 + s3 + t3 + ...
  or
    t1 + s1 + t2 + s2 + t3 + s3 + ...

Note:
    a + b denotes the concatenation of strings a and b.

Example 1:
    Input:
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
    Output: True
    Explanation:
        s3 can be formed by interleaving s1 and s2.

Example 2:
    Input:
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
    Output: False
    Explanation:
        It is impossible to interleave s1 and s2 to form s3.

Example 3:
    Input:
        s1 = ""
        s2 = ""
        s3 = ""
    Output: True

Constraints:
    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.
'''

# Dynamic Programming (1D DP)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [False] * (len(s2) + 1)
        dp[0] = True

        # Initialize first row
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Fill DP row by row
        for i in range(1, len(s1) + 1):

            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, len(s2) + 1):
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1])
                    or
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[-1]


# Example usage
solution = Solution()

print(solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # Output: True
print(solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # Output: False
print(solution.isInterleave("", "", ""))  # Output: True
print(solution.isInterleave("abc", "def", "adbcef"))  # Output: True
