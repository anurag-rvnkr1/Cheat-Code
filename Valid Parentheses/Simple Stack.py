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
#Simple Stack Solution
class Solution:
    def isValid(self, s):

        stack = []

        for ch in s:

            # If opening bracket
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            else:
                # If stack empty → invalid
                if not stack:
                    return False

                top = stack.pop()

                # Check matching
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        # If stack empty → valid
        return len(stack) == 0
#example usage
sol = Solution()
print(sol.isValid("()")) # True
print(sol.isValid("()[]{}")) # True