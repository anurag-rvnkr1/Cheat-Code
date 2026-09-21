'''
241. Different Ways to Add Parentheses

Given a string expression of numbers and operators, return all possible results
from computing all the different possible ways to group numbers and operators.

You may return the answer in any order.

The valid operators are '+', '-', and '*'.

Example 1:
    Input: expression = "2-1-1"
    Output: [0,2]

Explanation:
    ((2-1)-1) = 0
    (2-(1-1)) = 2

Example 2:
    Input: expression = "2*3-4*5"
    Output: [-34,-14,-10,-10,10]

Explanation:
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10

Constraints:
    1 <= expression.length <= 20
    expression consists of digits and the operators '+', '-', '*'.
    All integer values in the input expression are in the range [0, 99].
'''

# Divide and Conquer + Memoization

from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def solve(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]

            results = []

            for i, char in enumerate(expr):
                if char in "+-*":
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i + 1:])

                    for left in left_results:
                        for right in right_results:
                            if char == "+":
                                results.append(left + right)
                            elif char == "-":
                                results.append(left - right)
                            else:
                                results.append(left * right)

            # Base case: expression is a single number.
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return solve(expression)


# Example usage
solution = Solution()

# Example 1
expression1 = "2-1-1"
print(sorted(solution.diffWaysToCompute(expression1)))
# Output: [0, 2]

# Example 2
expression2 = "2*3-4*5"
print(sorted(solution.diffWaysToCompute(expression2)))
# Output: [-34, -14, -10, -10, 10]

# Example 3
expression3 = "11"
print(solution.diffWaysToCompute(expression3))
# Output: [11]

# Example 4
expression4 = "2+3*2"
print(sorted(solution.diffWaysToCompute(expression4)))
# Output: [8, 10]
