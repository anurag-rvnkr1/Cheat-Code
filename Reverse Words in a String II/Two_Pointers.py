'''
186. Reverse Words in a String II

Given a character array s, reverse the order of the words in-place.

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
Words are always separated by a single space.

You must solve it in-place with O(1) extra space.

Example 1:
    Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Example 2:
    Input: s = ["a"]
    Output: ["a"]

Constraints:
    1 <= s.length <= 10^5
    s[i] is an English letter, digit, or space.
    There is at least one word in s.
    s does not contain leading or trailing spaces.
    All words are separated by a single space.
'''

# Two Pointers (In-Place Reversal)

from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:

        # Helper function to reverse characters between two indices.
        def reverse(left: int, right: int):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Step 1: Reverse the entire character array.
        reverse(0, len(s) - 1)

        # Step 2: Reverse each word individually.
        start = 0

        for end in range(len(s) + 1):
            if end == len(s) or s[end] == " ":
                reverse(start, end - 1)
                start = end + 1


# Example usage
solution = Solution()

# Example 1
s1 = list("the sky is blue")
solution.reverseWords(s1)
print("".join(s1))  # Output: "blue is sky the"

# Example 2
s2 = list("hello world")
solution.reverseWords(s2)
print("".join(s2))  # Output: "world hello"

# Example 3
s3 = list("a")
solution.reverseWords(s3)
print("".join(s3))  # Output: "a"
