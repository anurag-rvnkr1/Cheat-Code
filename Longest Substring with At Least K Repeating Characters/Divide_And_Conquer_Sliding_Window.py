'''
395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k, return the length of the longest substring
of s such that the frequency of each character in this substring is greater
than or equal to k.

Example 1:
    Input:
        s = "aaabb"
        k = 3

    Output:
        3

Explanation:
        The longest substring is "aaa".

Example 2:
    Input:
        s = "ababbc"
        k = 2

    Output:
        5

Explanation:
        The longest substring is "ababb".

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
    1 <= k <= 10^5
'''

# Divide and Conquer + Sliding Window

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        frequency = Counter(s)

        for character, count in frequency.items():
            if count < k:
                return max(
                    self.longestSubstring(substring, k)
                    for substring in s.split(character)
                )

        return len(s)


# Example usage
solution = Solution()

# Example 1
s1 = "aaabb"
k1 = 3
print(solution.longestSubstring(s1, k1))
# Output: 3

# Example 2
s2 = "ababbc"
k2 = 2
print(solution.longestSubstring(s2, k2))
# Output: 5

# Example 3
s3 = "ababacb"
k3 = 3
print(solution.longestSubstring(s3, k3))
# Output: 0

# Example 4
s4 = "aaabbb"
k4 = 3
print(solution.longestSubstring(s4, k4))
# Output: 6

# Example 5
s5 = "weitong"
k5 = 2
print(solution.longestSubstring(s5, k5))
# Output: 0

# Example 6
s6 = "aabcccccaaa"
k6 = 2
print(solution.longestSubstring(s6, k6))
# Output: 11
