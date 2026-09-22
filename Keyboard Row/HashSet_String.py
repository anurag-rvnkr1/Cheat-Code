'''
500. Keyboard Row

Given an array of strings words, return the words that can be typed using
letters from only one row of an American keyboard.

Keyboard Rows:
    Row 1 : qwertyuiop
    Row 2 : asdfghjkl
    Row 3 : zxcvbnm

Example 1:
    Input:
        words = ["Hello","Alaska","Dad","Peace"]

    Output:
        ["Alaska","Dad"]

Example 2:
    Input:
        words = ["omk"]

    Output:
        []

Example 3:
    Input:
        words = ["adsdf","sfd"]

    Output:
        ["adsdf","sfd"]

Constraints:
    1 <= words.length <= 20
    1 <= words[i].length <= 100
    words[i] consists of English letters.
'''

# HashSet + String

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        answer = []

        for word in words:
            lowercase_word = set(word.lower())

            if (
                lowercase_word <= row1 or
                lowercase_word <= row2 or
                lowercase_word <= row3
            ):
                answer.append(word)

        return answer


# Example usage
solution = Solution()

# Example 1
words1 = ["Hello","Alaska","Dad","Peace"]
print(solution.findWords(words1))
# Output: ["Alaska","Dad"]

# Example 2
words2 = ["omk"]
print(solution.findWords(words2))
# Output: []

# Example 3
words3 = ["adsdf","sfd"]
print(solution.findWords(words3))
# Output: ["adsdf","sfd"]

# Example 4
words4 = ["QWERTY","TYPE","POP","LOL","MOM"]
print(solution.findWords(words4))
# Output: ["QWERTY","TYPE","POP"]

# Example 5
words5 = ["zxc","vbn","m","asdf","poiuy"]
print(solution.findWords(words5))
# Output: ["zxc","vbn","m","asdf","poiuy"]

# Example 6
words6 = ["Dad","Tree","Gas","Milk","Alaska","Queen"]
print(solution.findWords(words6))
# Output: ["Dad","Alaska"]
