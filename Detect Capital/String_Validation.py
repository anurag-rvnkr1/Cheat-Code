"""
520. Detect Capital

We define the usage of capitals in a word to be right when one of the
following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Given a string word, return True if the usage of capitals is right.
Otherwise, return False.

Examples:
1. Input: word = "USA"
   Output: True

2. Input: word = "FlaG"
   Output: False

3. Input: word = "leetcode"
   Output: True

4. Input: word = "Google"
   Output: True

5. Input: word = "mL"
   Output: False

6. Input: word = "A"
   Output: True
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


# Example 1
word = "USA"
print(Solution().detectCapitalUse(word))  # True

# Example 2
word = "FlaG"
print(Solution().detectCapitalUse(word))  # False

# Example 3
word = "leetcode"
print(Solution().detectCapitalUse(word))  # True

# Example 4
word = "Google"
print(Solution().detectCapitalUse(word))  # True

# Example 5
word = "mL"
print(Solution().detectCapitalUse(word))  # False

# Example 6
word = "A"
print(Solution().detectCapitalUse(word))  # True


# Time Complexity: O(n)
# Space Complexity: O(1)
