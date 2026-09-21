'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: True

Example 2:
    Input: s = "foo", t = "bar"
    Output: False

Example 3:
    Input: s = "paper", t = "title"
    Output: True

Constraints:
    1 <= s.length <= 5 * 10^4
    t.length == s.length
    s and t consist of any valid ASCII character.
'''

# HashMap


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):

            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


# Example usage
solution = Solution()

# Example 1
s1 = "egg"
t1 = "add"
print(solution.isIsomorphic(s1, t1))  # Output: True

# Example 2
s2 = "foo"
t2 = "bar"
print(solution.isIsomorphic(s2, t2))  # Output: False

# Example 3
s3 = "paper"
t3 = "title"
print(solution.isIsomorphic(s3, t3))  # Output: True

# Example 4
s4 = "badc"
t4 = "baba"
print(solution.isIsomorphic(s4, t4))  # Output: False
