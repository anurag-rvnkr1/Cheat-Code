'''
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression
in Reverse Polish Notation.

Evaluate the expression and return an integer that represents the value of the expression.

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
Division between two integers always truncates toward zero.

Example 1:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9

Explanation:
    ((2 + 1) * 3) = 9

Example 2:
    Input: tokens = ["4","13","5","/","+"]
    Output: 6

Explanation:
    (4 + (13 / 5)) = 6

Example 3:
    Input: tokens = [
        "10","6","9","3","+","-11","*","/","*","17","+","5","+"
    ]
    Output: 22

Explanation:
    ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22

Constraints:
    1 <= tokens.length <= 10^4
    tokens[i] is either an operator ("+", "-", "*", "/") or an integer
    in the range [-200, 200].
    The input is a valid Reverse Polish expression.
'''

# Stack

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    # Truncate division toward zero.
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[-1]


# Example usage
solution = Solution()

# Example 1
tokens1 = ["2", "1", "+", "3", "*"]
print(solution.evalRPN(tokens1))  # Output: 9

# Example 2
tokens2 = ["4", "13", "5", "/", "+"]
print(solution.evalRPN(tokens2))  # Output: 6

# Example 3
tokens3 = [
    "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
]
print(solution.evalRPN(tokens3))  # Output: 22

# Example 4
tokens4 = ["18", "3", "/"]
print(solution.evalRPN(tokens4))  # Output: 6
