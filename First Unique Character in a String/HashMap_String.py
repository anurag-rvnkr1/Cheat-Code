'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it
and return its index.

If it does not exist, return -1.

Example 1:
    Input:
        s = "leetcode"

    Output:
        0

Example 2:
    Input:
        s = "loveleetcode"

    Output:
        2

Example 3:
    Input:
        s = "aabb"

    Output:
        -1

Constraints:
    1 <= s.length <= 10^5
    s consists of only lowercase English letters.
'''

# HashMap / Character Frequency Counting

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = Counter(s)

        for index, character in enumerate(s):
            if frequency[character] == 1:
                return index

        return -1


# Example usage
solution = Solution()

# Example 1
s1 = "leetcode"
print(solution.firstUniqChar(s1))
# Output: 0

# Example 2
s2 = "loveleetcode"
print(solution.firstUniqChar(s2))
# Output: 2

# Example 3
s3 = "aabb"
print(solution.firstUniqChar(s3))
# Output: -1

# Example 4
s4 = "z"
print(solution.firstUniqChar(s4))
# Output: 0

# Example 5
s5 = "abcabcde"
print(solution.firstUniqChar(s5))
# Output: 6

# Example 6
s6 = "xxyyzzw"
print(solution.firstUniqChar(s6))
# Output: 6
