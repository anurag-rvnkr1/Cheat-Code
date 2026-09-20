'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True

Explanation:
    "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: False

Explanation:
    "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: True

Explanation:
    After removing non-alphanumeric characters, s becomes an empty string.
    An empty string is considered a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
'''

# Two Pointers


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Example usage
solution = Solution()

# Example 1
s1 = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s1))  # Output: True

# Example 2
s2 = "race a car"
print(solution.isPalindrome(s2))  # Output: False

# Example 3
s3 = " "
print(solution.isPalindrome(s3))  # Output: True

# Example 4
s4 = "0P"
print(solution.isPalindrome(s4))  # Output: False
