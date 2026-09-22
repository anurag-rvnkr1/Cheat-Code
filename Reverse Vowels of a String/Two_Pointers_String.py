'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string
and return the resulting string.

The vowels are:
    'a', 'e', 'i', 'o', 'u'
    and their uppercase counterparts.

Example 1:
    Input:
        s = "hello"

    Output:
        "holle"

Example 2:
    Input:
        s = "leetcode"

    Output:
        "leotcede"

Constraints:
    1 <= s.length <= 3 * 10^5
    s consists of printable ASCII characters.
'''

# Two Pointers + String Manipulation

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'
        }

        characters = list(s)

        left = 0
        right = len(characters) - 1

        while left < right:

            while left < right and characters[left] not in vowels:
                left += 1

            while left < right and characters[right] not in vowels:
                right -= 1

            characters[left], characters[right] = (
                characters[right],
                characters[left]
            )

            left += 1
            right -= 1

        return "".join(characters)


# Example usage
solution = Solution()

# Example 1
s1 = "hello"
print(solution.reverseVowels(s1))
# Output: "holle"

# Example 2
s2 = "leetcode"
print(solution.reverseVowels(s2))
# Output: "leotcede"

# Example 3
s3 = "aA"
print(solution.reverseVowels(s3))
# Output: "Aa"

# Example 4
s4 = "IceCreAm"
print(solution.reverseVowels(s4))
# Output: "AceCreIm"

# Example 5
s5 = "programming"
print(solution.reverseVowels(s5))
# Output: "prigrammong"

# Example 6
s6 = "AEIOUxyz"
print(solution.reverseVowels(s6))
# Output: "UOIEAxyz"
