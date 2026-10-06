"""
521. Longest Uncommon Subsequence I

Given two strings a and b, find the length of the longest uncommon
subsequence between them.

A subsequence is a sequence that can be derived from another string by
deleting some or no characters without changing the order of the
remaining characters.

An uncommon subsequence is a subsequence that is not a subsequence of
the other string.

If there is no possible uncommon subsequence, return -1.

Examples:
1. Input: a = "aba", b = "cdc"
   Output: 3

2. Input: a = "aaa", b = "bbb"
   Output: 3

3. Input: a = "aaa", b = "aaa"
   Output: -1

4. Input: a = "abc", b = "ab"
   Output: 3

5. Input: a = "abcd", b = "abc"
   Output: 4

6. Input: a = "a", b = "b"
   Output: 1
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1

        return max(len(a), len(b))


# Example 1
a = "aba"
b = "cdc"
print(Solution().findLUSlength(a, b))  # 3

# Example 2
a = "aaa"
b = "bbb"
print(Solution().findLUSlength(a, b))  # 3

# Example 3
a = "aaa"
b = "aaa"
print(Solution().findLUSlength(a, b))  # -1

# Example 4
a = "abc"
b = "ab"
print(Solution().findLUSlength(a, b))  # 3

# Example 5
a = "abcd"
b = "abc"
print(Solution().findLUSlength(a, b))  # 4

# Example 6
a = "a"
b = "b"
print(Solution().findLUSlength(a, b))  # 1


# Time Complexity: O(1)
# Space Complexity: O(1)
