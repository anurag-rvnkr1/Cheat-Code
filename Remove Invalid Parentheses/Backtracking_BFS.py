'''
301. Remove Invalid Parentheses

Given a string s that contains parentheses and letters, remove the minimum
number of invalid parentheses to make the input string valid.

Return all possible results after removing the minimum number of invalid
parentheses. Return the answer in any order.

Example 1:
    Input: s = "()())()"
    Output: ["(())()","()()()"]

Example 2:
    Input: s = "(a)())()"
    Output: ["(a())()","(a)()()"]

Example 3:
    Input: s = ")("
    Output: [""]

Constraints:
    1 <= s.length <= 25
    s consists of lowercase English letters and parentheses '(' and ')'.
    There will be at most 20 parentheses in s.
'''

# Backtracking + BFS

from typing import List
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def is_valid(string: str) -> bool:
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        result = []
        visited = {s}
        queue = deque([s])
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            for i in range(len(current)):
                if current[i] not in "()":
                    continue

                next_state = current[:i] + current[i + 1:]

                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

        return result


# Example usage
solution = Solution()

# Example 1
s1 = "()())()"
print(sorted(solution.removeInvalidParentheses(s1)))
# Output: ['(())()', '()()()']

# Example 2
s2 = "(a)())()"
print(sorted(solution.removeInvalidParentheses(s2)))
# Output: ['(a())()', '(a)()()']

# Example 3
s3 = ")("
print(solution.removeInvalidParentheses(s3))
# Output: ['']

# Example 4
s4 = "((()"
print(solution.removeInvalidParentheses(s4))
# Output: ['()']

# Example 5
s5 = "(())"
print(solution.removeInvalidParentheses(s5))
# Output: ['(())']
