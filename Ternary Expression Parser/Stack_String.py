'''
439. Ternary Expression Parser

Given a string expression representing a nested ternary expression,
evaluate it and return the result as a string.

The ternary expression is right-to-left associative.

Expression format:
    condition ? expression1 : expression2

Conditions are always:
    'T' -> True
    'F' -> False

Operands are single digits or uppercase letters.

Example 1:
    Input:
        expression = "T?2:3"

    Output:
        "2"

Example 2:
    Input:
        expression = "F?1:T?4:5"

    Output:
        "4"

Example 3:
    Input:
        expression = "T?T?F:5:3"

    Output:
        "F"

Constraints:
    5 <= expression.length <= 10^4
    expression consists of digits, letters, '?', ':', 'T', and 'F'.
    The input is guaranteed to be a valid ternary expression.
'''

# Stack + String Parsing

class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        # Traverse from right to left because ternary is right-associative.
        for character in reversed(expression):

            if stack and stack[-1] == "?":
                stack.pop()              # Remove '?'

                true_value = stack.pop() # Expression after '?'

                stack.pop()              # Remove ':'

                false_value = stack.pop()

                if character == "T":
                    stack.append(true_value)
                else:
                    stack.append(false_value)

            else:
                stack.append(character)

        return stack[-1]


# Example usage
solution = Solution()

# Example 1
expression1 = "T?2:3"
print(solution.parseTernary(expression1))
# Output: "2"

# Example 2
expression2 = "F?1:T?4:5"
print(solution.parseTernary(expression2))
# Output: "4"

# Example 3
expression3 = "T?T?F:5:3"
print(solution.parseTernary(expression3))
# Output: "F"

# Example 4
expression4 = "F?T?1:2:F?3:4"
print(solution.parseTernary(expression4))
# Output: "4"

# Example 5
expression5 = "T?F?1:2:3"
print(solution.parseTernary(expression5))
# Output: "2"

# Example 6
expression6 = "F?9:8"
print(solution.parseTernary(expression6))
# Output: "8"
