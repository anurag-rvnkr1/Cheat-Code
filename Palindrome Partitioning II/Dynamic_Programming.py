'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: 1

Explanation:
    The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
    Input: s = "a"
    Output: 0

Example 3:
    Input: s = "ab"
    Output: 1

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters only.
'''

# Dynamic Programming

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_palindrome[i][j] = True if s[i:j+1] is a palindrome.
        is_palindrome = [[False] * n for _ in range(n)]

        # cuts[i] = minimum cuts needed for s[:i+1].
        cuts = [0] * n

        for end in range(n):
            cuts[end] = end  # Maximum cuts possible.

            for start in range(end + 1):
                if (
                    s[start] == s[end]
                    and (end - start <= 2 or is_palindrome[start + 1][end - 1])
                ):
                    is_palindrome[start][end] = True

                    if start == 0:
                        cuts[end] = 0
                    else:
                        cuts[end] = min(cuts[end], cuts[start - 1] + 1)

        return cuts[-1]


# Example usage
solution = Solution()

# Example 1
s1 = "aab"
print(solution.minCut(s1))  # Output: 1

# Example 2
s2 = "a"
print(solution.minCut(s2))  # Output: 0

# Example 3
s3 = "ab"
print(solution.minCut(s3))  # Output: 1

# Example 4
s4 = "aabaa"
print(solution.minCut(s4))  # Output: 0
