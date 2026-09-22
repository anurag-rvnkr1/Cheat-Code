'''
340. Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest
substring of s that contains at most k distinct characters.

Example 1:
    Input:
        s = "eceba"
        k = 2

    Output:
        3

Explanation:
        "ece" contains at most 2 distinct characters.

Example 2:
    Input:
        s = "aa"
        k = 1

    Output:
        2

Constraints:
    1 <= s.length <= 5 * 10^4
    0 <= k <= 50
    s consists of English letters.
'''

# Sliding Window + HashMap

from typing import Dict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if k == 0:
            return 0

        left = 0
        maximum_length = 0

        frequency: Dict[str, int] = {}

        for right in range(len(s)):

            frequency[s[right]] = frequency.get(s[right], 0) + 1

            while len(frequency) > k:

                frequency[s[left]] -= 1

                if frequency[s[left]] == 0:
                    del frequency[s[left]]

                left += 1

            maximum_length = max(
                maximum_length,
                right - left + 1
            )

        return maximum_length


# Example usage
solution = Solution()

# Example 1
s1 = "eceba"
k1 = 2
print(solution.lengthOfLongestSubstringKDistinct(s1, k1))
# Output: 3

# Example 2
s2 = "aa"
k2 = 1
print(solution.lengthOfLongestSubstringKDistinct(s2, k2))
# Output: 2

# Example 3
s3 = "abcadcacacaca"
k3 = 3
print(solution.lengthOfLongestSubstringKDistinct(s3, k3))
# Output: 11

# Example 4
s4 = "world"
k4 = 4
print(solution.lengthOfLongestSubstringKDistinct(s4, k4))
# Output: 4

# Example 5
s5 = "aabbcc"
k5 = 2
print(solution.lengthOfLongestSubstringKDistinct(s5, k5))
# Output: 4

# Example 6
s6 = "abc"
k6 = 0
print(solution.lengthOfLongestSubstringKDistinct(s6, k6))
# Output: 0
