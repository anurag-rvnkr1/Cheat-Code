'''
418. Sentence Screen Fitting

Given a rows x cols screen and a sentence represented as a list of strings,
return the number of times the sentence can fit on the screen.

Rules:
    - Words must remain in the original order.
    - A word cannot be split across lines.
    - Consecutive words are separated by a single space.

Example 1:
    Input:
        sentence = ["hello","world"]
        rows = 2
        cols = 8

    Output:
        1

Example 2:
    Input:
        sentence = ["a","bcd","e"]
        rows = 3
        cols = 6

    Output:
        2

Example 3:
    Input:
        sentence = ["i","had","apple","pie"]
        rows = 4
        cols = 5

    Output:
        1

Constraints:
    1 <= sentence.length <= 100
    1 <= rows, cols <= 2 * 10^4
    1 <= sentence[i].length <= 10
    sentence[i] consists of lowercase English letters.
'''

# Greedy + String + DP

from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence_string = " ".join(sentence) + " "
        length = len(sentence_string)

        position = 0

        for _ in range(rows):
            position += cols

            if sentence_string[position % length] == " ":
                position += 1
            else:
                while position > 0 and sentence_string[(position - 1) % length] != " ":
                    position -= 1

        return position // length


# Example usage
solution = Solution()

# Example 1
sentence1 = ["hello","world"]
rows1 = 2
cols1 = 8
print(solution.wordsTyping(sentence1, rows1, cols1))
# Output: 1

# Example 2
sentence2 = ["a","bcd","e"]
rows2 = 3
cols2 = 6
print(solution.wordsTyping(sentence2, rows2, cols2))
# Output: 2

# Example 3
sentence3 = ["i","had","apple","pie"]
rows3 = 4
cols3 = 5
print(solution.wordsTyping(sentence3, rows3, cols3))
# Output: 1

# Example 4
sentence4 = ["abc","de","f"]
rows4 = 4
cols4 = 6
print(solution.wordsTyping(sentence4, rows4, cols4))
# Output: 2

# Example 5
sentence5 = ["a"]
rows5 = 5
cols5 = 1
print(solution.wordsTyping(sentence5, rows5, cols5))
# Output: 5

# Example 6
sentence6 = ["leetcode","is","awesome"]
rows6 = 5
cols6 = 15
print(solution.wordsTyping(sentence6, rows6, cols6))
# Output: 2
