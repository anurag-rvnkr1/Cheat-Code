'''
266. Palindrome Permutation

Given a string s, return True if a permutation of the string could form
a palindrome, otherwise return False.

A string can be rearranged to form a palindrome if:
    - Every character appears an even number of times.
    - At most one character appears an odd number of times.

Example 1:
    Input: s = "code"
    Output: False

Example 2:
    Input: s = "aab"
    Output: True

Explanation:
    "aab" can be rearranged as "aba".

Example 3:
    Input: s = "carerac"
    Output: True

Explanation:
    "carerac" can be rearranged as "racecar".

Constraints:
    1 <= s.length <= 5000
    s consists of lowercase English letters.
'''

# HashMap + String


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        frequency = {}

        # Count frequency of each character.
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        odd_count = 0

        # Count characters with odd frequencies.
        for count in frequency.values():
            if count % 2 == 1:
                odd_count += 1

            if odd_count > 1:
                return False

        return True


# Example usage
solution = Solution()

# Example 1
s1 = "code"
print(solution.canPermutePalindrome(s1))
# Output: False

# Example 2
s2 = "aab"
print(solution.canPermutePalindrome(s2))
# Output: True

# Example 3
s3 = "carerac"
print(solution.canPermutePalindrome(s3))
# Output: True

# Example 4
s4 = "aabbcc"
print(solution.canPermutePalindrome(s4))
# Output: True

# Example 5
s5 = "abcabcad"
print(solution.canPermutePalindrome(s5))
# Output: False
