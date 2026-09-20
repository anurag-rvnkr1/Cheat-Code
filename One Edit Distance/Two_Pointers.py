'''
161. One Edit Distance

Given two strings s and t, return True if they are exactly one edit distance apart.

An edit is one of the following operations performed exactly once:

    - Insert one character into a string.
    - Delete one character from a string.
    - Replace one character in a string.

Return False if the strings are zero edits apart or more than one edit apart.

Example 1:
    Input: s = "ab", t = "acb"
    Output: True

Explanation:
    Insert 'c' into s to get "acb".

Example 2:
    Input: s = "cab", t = "ad"
    Output: False

Example 3:
    Input: s = "1203", t = "1213"
    Output: True

Constraints:
    0 <= s.length, t.length <= 10^4
    s and t consist of lowercase English letters.
'''

# Two Pointers


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # Ensure s is the shorter string.
        if m > n:
            return self.isOneEditDistance(t, s)

        # Length difference greater than 1 is impossible.
        if n - m > 1:
            return False

        for i in range(m):
            if s[i] != t[i]:
                # Replace operation.
                if m == n:
                    return s[i + 1:] == t[i + 1:]

                # Insert/Delete operation.
                return s[i:] == t[i + 1:]

        # Strings are identical only if t has one extra character.
        return m + 1 == n


# Example usage
solution = Solution()

# Example 1
s1 = "ab"
t1 = "acb"
print(solution.isOneEditDistance(s1, t1))  # Output: True

# Example 2
s2 = "cab"
t2 = "ad"
print(solution.isOneEditDistance(s2, t2))  # Output: False

# Example 3
s3 = "1203"
t3 = "1213"
print(solution.isOneEditDistance(s3, t3))  # Output: True

# Example 4
s4 = "abc"
t4 = "abc"
print(solution.isOneEditDistance(s4, t4))  # Output: False
