'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition
is a palindrome.

Return all possible palindrome partitioning of s.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
'''

# Backtracking

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result


# Example usage
solution = Solution()

# Example 1
s1 = "aab"
print(solution.partition(s1))
# Output: [['a', 'a', 'b'], ['aa', 'b']]

# Example 2
s2 = "a"
print(solution.partition(s2))
# Output: [['a']]

# Example 3
s3 = "efe"
print(solution.partition(s3))
# Output: [['e', 'f', 'e'], ['efe']]
