'''
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator
to evaluate it and return the result of the evaluation.

Note:
    - You are not allowed to use any built-in function which evaluates strings
      as mathematical expressions.
    - The expression may contain '+', '-', '(', ')', digits, and spaces.

Example 1:
    Input: s = "1 + 1"
    Output: 2

Example 2:
    Input: s = " 2-1 + 2 "
    Output: 3

Example 3:
    Input: s = "(1+(4+5+2)-3)+(6+8)"
    Output: 23

Constraints:
    1 <= s.length <= 3 * 10^5
    s consists of digits, '+', '-', '(', ')', and spaces.
    s represents a valid expression.
'''

# Stack


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1

        for char in s:

            if char.isdigit():
                number = number * 10 + int(char)

            elif char == "+":
                result += sign * number
                number = 0
                sign = 1

            elif char == "-":
                result += sign * number
                number = 0
                sign = -1

            elif char == "(":
                # Save current result and sign.
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif char == ")":
                result += sign * number
                number = 0

                # Multiply with sign before '('.
                result *= stack.pop()

                # Add result before '('.
                result += stack.pop()

        result += sign * number

        return result


# Example usage
solution = Solution()

# Example 1
s1 = "1 + 1"
print(solution.calculate(s1))  # Output: 2

# Example 2
s2 = " 2-1 + 2 "
print(solution.calculate(s2))  # Output: 3

# Example 3
s3 = "(1+(4+5+2)-3)+(6+8)"
print(solution.calculate(s3))  # Output: 23

# Example 4
s4 = "10-(2+(3-1))"
print(solution.calculate(s4))  # Output: 6
