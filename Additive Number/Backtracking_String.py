'''
306. Additive Number

An additive number is a string whose digits can form an additive sequence.

A valid additive sequence:
    - Contains at least three numbers.
    - Except for the number 0 itself, numbers cannot have leading zeros.
    - Starting from the third number, every number equals the sum of the previous two.

Return True if num is an additive number, otherwise return False.

Example 1:
    Input: num = "112358"
    Output: True

Explanation:
    Sequence: 1, 1, 2, 3, 5, 8

Example 2:
    Input: num = "199100199"
    Output: True

Explanation:
    Sequence: 1, 99, 100, 199

Example 3:
    Input: num = "1023"
    Output: False

Constraints:
    1 <= num.length <= 35
    num consists only of digits.
'''

# Backtracking + String


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Choose first number.
        for i in range(1, n):

            # Skip leading zeros.
            if num[0] == "0" and i > 1:
                break

            first = int(num[:i])

            # Choose second number.
            for j in range(i + 1, n):

                # Skip leading zeros.
                if num[i] == "0" and j - i > 1:
                    break

                second = int(num[i:j])

                if self._is_valid_sequence(first, second, j, num):
                    return True

        return False

    def _is_valid_sequence(
        self,
        first: int,
        second: int,
        index: int,
        num: str
    ) -> bool:

        while index < len(num):
            third = first + second
            third_string = str(third)

            if not num.startswith(third_string, index):
                return False

            index += len(third_string)
            first, second = second, third

        return True


# Example usage
solution = Solution()

# Example 1
num1 = "112358"
print(solution.isAdditiveNumber(num1))
# Output: True

# Example 2
num2 = "199100199"
print(solution.isAdditiveNumber(num2))
# Output: True

# Example 3
num3 = "1023"
print(solution.isAdditiveNumber(num3))
# Output: False

# Example 4
num4 = "000"
print(solution.isAdditiveNumber(num4))
# Output: True

# Example 5
num5 = "123581321"
print(solution.isAdditiveNumber(num5))
# Output: True

# Example 6
num6 = "111122335588143"
print(solution.isAdditiveNumber(num6))
# Output: False
