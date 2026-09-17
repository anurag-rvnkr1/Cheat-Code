'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.

If there is no such substring, return the empty string "".

The test cases will be generated such that the answer is unique.

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation:
    The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation:
    The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation:
    Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return an empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 10^5
    s and t consist of uppercase and lowercase English letters.
'''

# Sliding Window + Hash Map
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0
        formed = 0
        required = len(need)

        min_length = float('inf')
        start = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Character has reached its required frequency
            if char in need and window[char] == need[char]:
                formed += 1

            # Try shrinking the window
            while formed == required:

                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_length == float('inf'):
            return ""

        return s[start:start + min_length]


# Example usage
solution = Solution()

print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))  # Output: "a"
print(solution.minWindow("a", "aa"))  # Output: ""
print(solution.minWindow("aa", "aa"))  # Output: "aa"
