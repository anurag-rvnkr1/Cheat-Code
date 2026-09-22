'''
392. Is Subsequence

Given two strings s and t, return True if s is a subsequence of t,
or False otherwise.

A subsequence is formed by deleting some (or no) characters from t
without changing the order of the remaining characters.

Example 1:
    Input:
        s = "abc"
        t = "ahbgdc"

    Output:
        True

Example 2:
    Input:
        s = "axc"
        t = "ahbgdc"

    Output:
        False

Constraints:
    0 <= s.length <= 100
    0 <= t.length <= 10^4
    s and t consist only of lowercase English letters.

Follow-up:
    If there are lots of incoming s strings, how would you optimize it?
'''

# Two Pointers

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointer_s = 0
        pointer_t = 0

        while pointer_s < len(s) and pointer_t < len(t):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1

            pointer_t += 1

        return pointer_s == len(s)


# Example usage
solution = Solution()

# Example 1
s1 = "abc"
t1 = "ahbgdc"
print(solution.isSubsequence(s1, t1))
# Output: True

# Example 2
s2 = "axc"
t2 = "ahbgdc"
print(solution.isSubsequence(s2, t2))
# Output: False

# Example 3
s3 = ""
t3 = "abc"
print(solution.isSubsequence(s3, t3))
# Output: True

# Example 4
s4 = "ace"
t4 = "abcde"
print(solution.isSubsequence(s4, t4))
# Output: True

# Example 5
s5 = "aec"
t5 = "abcde"
print(solution.isSubsequence(s5, t5))
# Output: False

# Example 6
s6 = "aaaa"
t6 = "aaabaa"
print(solution.isSubsequence(s6, t6))
# Output: True
