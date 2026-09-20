'''
159. Longest Substring with At Most Two Distinct Characters

Given a string s, return the length of the longest substring that contains
at most two distinct characters.

Example 1:
    Input: s = "eceba"
    Output: 3

Explanation:
    The substring is "ece" with length 3.

Example 2:
    Input: s = "ccaabbb"
    Output: 5

Explanation:
    The substring is "aabbb" with length 5.

Example 3:
    Input: s = "a"
    Output: 1

Constraints:
    1 <= s.length <= 10^5
    s consists of English letters.
'''

# Sliding Window

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        longest = 0
        frequency = defaultdict(int)

        for right in range(len(s)):
            frequency[s[right]] += 1

            # Shrink window until it contains at most 2 distinct characters.
            while len(frequency) > 2:
                frequency[s[left]] -= 1

                if frequency[s[left]] == 0:
                    del frequency[s[left]]

                left += 1

            longest = max(longest, right - left + 1)

        return longest


# Example usage
solution = Solution()

# Example 1
s1 = "eceba"
print(solution.lengthOfLongestSubstringTwoDistinct(s1))  # Output: 3

# Example 2
s2 = "ccaabbb"
print(solution.lengthOfLongestSubstringTwoDistinct(s2))  # Output: 5

# Example 3
s3 = "a"
print(solution.lengthOfLongestSubstringTwoDistinct(s3))  # Output: 1

# Example 4
s4 = "abcabcabc"
print(solution.lengthOfLongestSubstringTwoDistinct(s4))  # Output: 2
