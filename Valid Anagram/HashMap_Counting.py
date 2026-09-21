'''
242. Valid Anagram

Given two strings s and t, return True if t is an anagram of s,
and False otherwise.

An anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: True

Example 2:
    Input: s = "rat", t = "car"
    Output: False

Constraints:
    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase English letters.

Follow-up:
    What if the inputs contain Unicode characters?
'''

# HashMap + Counting


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings with different lengths cannot be anagrams.
        if len(s) != len(t):
            return False

        frequency = {}

        # Count characters in s.
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        # Remove counts using t.
        for char in t:
            if char not in frequency:
                return False

            frequency[char] -= 1

            if frequency[char] == 0:
                del frequency[char]

        return len(frequency) == 0


# Example usage
solution = Solution()

# Example 1
s1 = "anagram"
t1 = "nagaram"
print(solution.isAnagram(s1, t1))  # Output: True

# Example 2
s2 = "rat"
t2 = "car"
print(solution.isAnagram(s2, t2))  # Output: False

# Example 3
s3 = "listen"
t3 = "silent"
print(solution.isAnagram(s3, t3))  # Output: True

# Example 4
s4 = "hello"
t4 = "bello"
print(solution.isAnagram(s4, t4))  # Output: False

# Example 5
s5 = "aacc"
t5 = "ccac"
print(solution.isAnagram(s5, t5))  # Output: False
