'''
316. Remove Duplicate Letters

Given a string s, remove duplicate letters so that every letter appears once
and only once.

You must return the smallest lexicographical result among all possible answers.

Example 1:
    Input:
        s = "bcabc"

    Output:
        "abc"

Example 2:
    Input:
        s = "cbacdcbc"

    Output:
        "acdb"

Explanation:
    Every letter appears exactly once.
    "acdb" is the smallest lexicographical valid string.

Constraints:
    1 <= s.length <= 10^4
    s consists of lowercase English letters.
'''

# Monotonic Stack + Greedy

from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        frequency = Counter(s)
        stack = []
        visited = set()

        for character in s:
            # Current character has been processed once.
            frequency[character] -= 1

            # Skip duplicate characters already in the answer.
            if character in visited:
                continue

            # Maintain lexicographically smallest stack.
            while (
                stack and
                character < stack[-1] and
                frequency[stack[-1]] > 0
            ):
                visited.remove(stack.pop())

            stack.append(character)
            visited.add(character)

        return "".join(stack)


# Example usage
solution = Solution()

# Example 1
s1 = "bcabc"
print(solution.removeDuplicateLetters(s1))
# Output: "abc"

# Example 2
s2 = "cbacdcbc"
print(solution.removeDuplicateLetters(s2))
# Output: "acdb"

# Example 3
s3 = "abacb"
print(solution.removeDuplicateLetters(s3))
# Output: "abc"

# Example 4
s4 = "bbcaac"
print(solution.removeDuplicateLetters(s4))
# Output: "bac"

# Example 5
s5 = "aaaa"
print(solution.removeDuplicateLetters(s5))
# Output: "a"

# Example 6
s6 = "ecbacba"
print(solution.removeDuplicateLetters(s6))
# Output: "eacb"
