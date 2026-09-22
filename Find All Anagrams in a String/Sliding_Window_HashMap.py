'''
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's
anagrams in s.

The answer may be returned in any order.

Example 1:
    Input:
        s = "cbaebabacd"
        p = "abc"

    Output:
        [0,6]

Explanation:
        The substrings "cba" and "bac" are anagrams of "abc".

Example 2:
    Input:
        s = "abab"
        p = "ab"

    Output:
        [0,1,2]

Constraints:
    1 <= s.length, p.length <= 3 * 10^4
    s and p consist of lowercase English letters.
'''

# Sliding Window + HashMap

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        target_frequency = [0] * 26
        window_frequency = [0] * 26

        for character in p:
            target_frequency[ord(character) - ord("a")] += 1

        result = []
        window_size = len(p)

        for index in range(len(s)):
            window_frequency[ord(s[index]) - ord("a")] += 1

            # Remove character leaving the sliding window.
            if index >= window_size:
                window_frequency[
                    ord(s[index - window_size]) - ord("a")
                ] -= 1

            # Compare both frequency arrays.
            if window_frequency == target_frequency:
                result.append(index - window_size + 1)

        return result


# Example usage
solution = Solution()

# Example 1
s1 = "cbaebabacd"
p1 = "abc"
print(solution.findAnagrams(s1, p1))
# Output: [0,6]

# Example 2
s2 = "abab"
p2 = "ab"
print(solution.findAnagrams(s2, p2))
# Output: [0,1,2]

# Example 3
s3 = "aaaaaaaaaa"
p3 = "aa"
print(solution.findAnagrams(s3, p3))
# Output: [0,1,2,3,4,5,6,7,8]

# Example 4
s4 = "af"
p4 = "be"
print(solution.findAnagrams(s4, p4))
# Output: []

# Example 5
s5 = "baa"
p5 = "aa"
print(solution.findAnagrams(s5, p5))
# Output: [1]

# Example 6
s6 = "abcabcabc"
p6 = "cab"
print(solution.findAnagrams(s6, p6))
# Output: [0,1,2,3,4,5,6]
