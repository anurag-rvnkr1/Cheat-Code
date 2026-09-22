'''
383. Ransom Note

Given two strings ransomNote and magazine, return True if ransomNote can be
constructed by using the letters from magazine.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input:
        ransomNote = "a"
        magazine = "b"

    Output:
        False

Example 2:
    Input:
        ransomNote = "aa"
        magazine = "ab"

    Output:
        False

Example 3:
    Input:
        ransomNote = "aa"
        magazine = "aab"

    Output:
        True

Constraints:
    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of lowercase English letters.
'''

# HashMap / Character Frequency Counting

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_frequency = Counter(magazine)

        for character in ransomNote:
            if magazine_frequency[character] == 0:
                return False

            magazine_frequency[character] -= 1

        return True


# Example usage
solution = Solution()

# Example 1
ransomNote1 = "a"
magazine1 = "b"
print(solution.canConstruct(ransomNote1, magazine1))
# Output: False

# Example 2
ransomNote2 = "aa"
magazine2 = "ab"
print(solution.canConstruct(ransomNote2, magazine2))
# Output: False

# Example 3
ransomNote3 = "aa"
magazine3 = "aab"
print(solution.canConstruct(ransomNote3, magazine3))
# Output: True

# Example 4
ransomNote4 = "leetcode"
magazine4 = "letcodexee"
print(solution.canConstruct(ransomNote4, magazine4))
# Output: True

# Example 5
ransomNote5 = "hello"
magazine5 = "helo"
print(solution.canConstruct(ransomNote5, magazine5))
# Output: False

# Example 6
ransomNote6 = "xyz"
magazine6 = "zxy"
print(solution.canConstruct(ransomNote6, magazine6))
# Output: True
