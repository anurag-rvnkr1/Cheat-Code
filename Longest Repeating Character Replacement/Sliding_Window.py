'''
424. Longest Repeating Character Replacement

You are given a string s and an integer k.

You can choose at most k characters in the string and replace them with any
uppercase English letter.

Return the length of the longest substring containing the same letter after
performing at most k replacements.

Example 1:
    Input:
        s = "ABAB"
        k = 2

    Output:
        4

Explanation:
        Replace the two 'A's with 'B's or vice versa.

Example 2:
    Input:
        s = "AABABBA"
        k = 1

    Output:
        4

Explanation:
        Replace one 'A' with 'B' to obtain "AABBBBA".

Constraints:
    1 <= s.length <= 10^5
    s consists of uppercase English letters.
    0 <= k <= s.length
'''

# Sliding Window

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)

        left = 0
        max_frequency = 0
        longest_window = 0

        for right in range(len(s)):
            frequency[s[right]] += 1

            max_frequency = max(max_frequency, frequency[s[right]])

            while (right - left + 1) - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1

            longest_window = max(longest_window, right - left + 1)

        return longest_window


# Example usage
solution = Solution()

# Example 1
s1 = "ABAB"
k1 = 2
print(solution.characterReplacement(s1, k1))
# Output: 4

# Example 2
s2 = "AABABBA"
k2 = 1
print(solution.characterReplacement(s2, k2))
# Output: 4

# Example 3
s3 = "AAAA"
k3 = 2
print(solution.characterReplacement(s3, k3))
# Output: 4

# Example 4
s4 = "ABCDE"
k4 = 1
print(solution.characterReplacement(s4, k4))
# Output: 2

# Example 5
s5 = "BAAAB"
k5 = 2
print(solution.characterReplacement(s5, k5))
# Output: 5

# Example 6
s6 = "ABBBAC"
k6 = 1
print(solution.characterReplacement(s6, k6))
# Output: 5
