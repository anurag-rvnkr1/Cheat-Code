'''
68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.

Example 1:
    Input:
        words = ["This","is","an","example","of","text","justification."]
        maxWidth = 16
    Output:
        [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]

Example 2:
    Input:
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
    Output:
        [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
    Explanation:
        The last line is left-justified instead of fully justified.
        The second line is also left-justified because it contains only one word.

Example 3:
    Input:
        words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
    Output:
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]

Constraints:
    1 <= words.length <= 300
    1 <= words[i].length <= 20
    words[i] consists of only English letters and symbols.
    1 <= maxWidth <= 100
    words[i].length <= maxWidth
'''

# Greedy Line Packing + Space Distribution
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            # Pack as many words as possible into the current line
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(w) for w in line_words)

            # Last line or single word → left justify
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                spaces = maxWidth - total_chars
                gaps = num_words - 1
                even = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (even + (1 if k < extra else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res


# Example usage
solution = Solution()

print(solution.fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16
))
# Output:
# ['This    is    an', 'example  of text', 'justification.  ']

print(solution.fullJustify(
    ["What", "must", "be", "acknowledgment", "shall", "be"], 16
))
# Output:
# ['What   must   be', 'acknowledgment  ', 'shall be        ']

print(solution.fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to",
     "explain", "to", "a", "computer.", "Art", "is", "everything", "else",
     "we", "do"], 20
))
# Output:
# [
# 'Science  is  what we',
# 'understand      well',
# 'enough to explain to',
# 'a  computer.  Art is',
# 'everything  else  we',
# 'do                  '
# ]
