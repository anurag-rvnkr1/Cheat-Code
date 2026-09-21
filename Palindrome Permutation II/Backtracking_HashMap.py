'''
267. Palindrome Permutation II

Given a string s, return all the palindromic permutations (without duplicates)
of s. Return the answer in any order.

If no palindromic permutation exists, return an empty list.

Example 1:
    Input: s = "aabb"
    Output: ["abba","baab"]

Example 2:
    Input: s = "abc"
    Output: []

Constraints:
    1 <= s.length <= 16
    s consists of lowercase English letters.
'''

# Backtracking + HashMap

from typing import List
from collections import Counter


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        frequency = Counter(s)

        odd_character = ""
        odd_count = 0
        half_string = []

        # Check palindrome possibility and build half string.
        for char, count in frequency.items():
            if count % 2 == 1:
                odd_count += 1
                odd_character = char

            if odd_count > 1:
                return []

            half_string.extend([char] * (count // 2))

        half_string.sort()
        result = []
        used = [False] * len(half_string)

        def backtrack(path):
            if len(path) == len(half_string):
                left_half = "".join(path)
                palindrome = left_half + odd_character + left_half[::-1]
                result.append(palindrome)
                return

            for i in range(len(half_string)):
                if used[i]:
                    continue

                # Skip duplicate characters.
                if (
                    i > 0 and
                    half_string[i] == half_string[i - 1] and
                    not used[i - 1]
                ):
                    continue

                used[i] = True
                path.append(half_string[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return result


# Example usage
solution = Solution()

# Example 1
s1 = "aabb"
print(sorted(solution.generatePalindromes(s1)))
# Output: ['abba', 'baab']

# Example 2
s2 = "abc"
print(solution.generatePalindromes(s2))
# Output: []

# Example 3
s3 = "aaa"
print(solution.generatePalindromes(s3))
# Output: ['aaa']

# Example 4
s4 = "aabbcc"
print(sorted(solution.generatePalindromes(s4)))
# Output:
# ['abccba', 'acbbca', 'baccab',
#  'bcaacb', 'cabbac', 'cbaabc']

# Example 5
s5 = "racecar"
print(sorted(solution.generatePalindromes(s5)))
# Output includes:
# ['acrerca', 'arcecra', 'carerac', ...]
