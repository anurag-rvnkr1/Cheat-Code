'''
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and
return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate
results will be in the range [-2^31, 2^31 - 1].

Note:
    - You are not allowed to use any built-in function which evaluates strings
      as mathematical expressions.
    - The expression contains non-negative integers, '+', '-', '*', '/',
      and spaces.

Example 1:
    Input: s = "3+2*2"
    Output: 7

Example 2:
    Input: s = " 3/2 "
    Output: 1

Example 3:
    Input: s = " 3+5 / 2 "
    Output: 5

Constraints:
    1 <= s.length <= 3 * 10^5
    s consists of integers and operators ('+', '-', '*', '/').
    s is a valid expression.
'''

# Stack + String Parsing


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        operator = "+"

        # Append '+' to process the last number.
        for char in s + "+":

            if char.isdigit():
                number = number * 10 + int(char)

            elif char == " ":
                continue

            else:
                if operator == "+":
                    stack.append(number)

                elif operator == "-":
                    stack.append(-number)

                elif operator == "*":
                    stack.append(stack.pop() * number)

                elif operator == "/":
                    previous = stack.pop()
                    stack.append(int(previous / number))

                operator = char
                number = 0

        return sum(stack)


# Example usage
solution = Solution()

# Example 1
s1 = "3+2*2"
print(solution.calculate(s1))  # Output: 7

# Example 2
s2 = " 3/2 "
print(solution.calculate(s2))  # Output: 1

# Example 3
s3 = " 3+5 / 2 "
print(solution.calculate(s3))  # Output: 5

# Example 4
s4 = "14-3/2"
print(solution.calculate(s4))  # Output: 13
