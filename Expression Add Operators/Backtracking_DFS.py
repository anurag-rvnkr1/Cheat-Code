'''
282. Expression Add Operators

Given a string num that contains only digits and an integer target,
return all possibilities to insert the binary operators '+', '-', and '*'
between the digits so that the resulting expression evaluates to target.

Return the answer in any order.

Note:
    - Operands cannot contain leading zeros.
    - Multiplication has higher precedence than addition and subtraction.

Example 1:
    Input: num = "123", target = 6
    Output: ["1+2+3","1*2*3"]

Example 2:
    Input: num = "232", target = 8
    Output: ["2*3+2","2+3*2"]

Example 3:
    Input: num = "3456237490", target = 9191
    Output: []

Constraints:
    1 <= num.length <= 10
    num consists of digits only.
    -2^31 <= target <= 2^31 - 1
'''

# Backtracking + DFS

from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(index, expression, current_value, previous_value):
            # Reached the end of the string.
            if index == len(num):
                if current_value == target:
                    result.append(expression)
                return

            for end in range(index, len(num)):
                # Skip numbers with leading zeros.
                if end > index and num[index] == "0":
                    break

                current_string = num[index:end + 1]
                current_number = int(current_string)

                # First number in the expression.
                if index == 0:
                    backtrack(
                        end + 1,
                        current_string,
                        current_number,
                        current_number
                    )

                else:
                    # Addition
                    backtrack(
                        end + 1,
                        expression + "+" + current_string,
                        current_value + current_number,
                        current_number
                    )

                    # Subtraction
                    backtrack(
                        end + 1,
                        expression + "-" + current_string,
                        current_value - current_number,
                        -current_number
                    )

                    # Multiplication
                    backtrack(
                        end + 1,
                        expression + "*" + current_string,
                        current_value - previous_value +
                        previous_value * current_number,
                        previous_value * current_number
                    )

        backtrack(0, "", 0, 0)
        return result


# Example usage
solution = Solution()

# Example 1
num1 = "123"
target1 = 6
print(sorted(solution.addOperators(num1, target1)))
# Output: ['1*2*3', '1+2+3']

# Example 2
num2 = "232"
target2 = 8
print(sorted(solution.addOperators(num2, target2)))
# Output: ['2*3+2', '2+3*2']

# Example 3
num3 = "105"
target3 = 5
print(sorted(solution.addOperators(num3, target3)))
# Output: ['1*0+5', '10-5']

# Example 4
num4 = "00"
target4 = 0
print(sorted(solution.addOperators(num4, target4)))
# Output: ['0*0', '0+0', '0-0']

# Example 5
num5 = "3456237490"
target5 = 9191
print(solution.addOperators(num5, target5))
# Output: []
