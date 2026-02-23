'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
'''
#HashMap + Stack Solution
class Solution:
    def isValid(self, s):

        stack = []

        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:

            # If closing bracket
            if ch in mapping:

                # Pop only if stack not empty
                top = stack.pop() if stack else '#'

                if mapping[ch] != top:
                    return False

            else:
                # Opening bracket
                stack.append(ch)

        return not stack
#example test case
sol= Solution()
print(sol.isValid("()[]{}"))
print(sol.isValid("([)]"))