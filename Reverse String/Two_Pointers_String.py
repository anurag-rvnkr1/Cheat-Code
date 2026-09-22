'''
344. Reverse String

Write a function that reverses a string.

The input string is given as an array of characters s.

You must modify the input array in-place with O(1) extra memory.

Example 1:
    Input:
        s = ["h","e","l","l","o"]

    Output:
        ["o","l","l","e","h"]

Example 2:
    Input:
        s = ["H","a","n","n","a","h"]

    Output:
        ["h","a","n","n","a","H"]

Constraints:
    1 <= s.length <= 10^5
    s[i] is a printable ASCII character.
'''

# Two Pointers + In-place String Manipulation

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything.
        Modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1


# Example usage
solution = Solution()

# Example 1
s1 = ["h", "e", "l", "l", "o"]
solution.reverseString(s1)
print(s1)
# Output: ['o', 'l', 'l', 'e', 'h']

# Example 2
s2 = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s2)
print(s2)
# Output: ['h', 'a', 'n', 'n', 'a', 'H']

# Example 3
s3 = ["a"]
solution.reverseString(s3)
print(s3)
# Output: ['a']

# Example 4
s4 = ["A", "B", "C", "D"]
solution.reverseString(s4)
print(s4)
# Output: ['D', 'C', 'B', 'A']

# Example 5
s5 = ["1", "2", "3", "4", "5"]
solution.reverseString(s5)
print(s5)
# Output: ['5', '4', '3', '2', '1']

# Example 6
s6 = ["x", "y"]
solution.reverseString(s6)
print(s6)
# Output: ['y', 'x']
