'''
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Example 1:
    Input: num = 38
    Output: 2

Explanation:
    38 -> 3 + 8 = 11
    11 -> 1 + 1 = 2

Example 2:
    Input: num = 0
    Output: 0

Constraints:
    0 <= num <= 2^31 - 1

Follow-up:
    Could you do it without any loop or recursion in O(1) time?
'''

# Math (Digital Root)


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        # Digital Root Formula
        return 1 + (num - 1) % 9


# Example usage
solution = Solution()

# Example 1
num1 = 38
print(solution.addDigits(num1))
# Output: 2

# Example 2
num2 = 0
print(solution.addDigits(num2))
# Output: 0

# Example 3
num3 = 99
print(solution.addDigits(num3))
# Output: 9

# Example 4
num4 = 12345
print(solution.addDigits(num4))
# Output: 6

# Example 5
num5 = 999999999
print(solution.addDigits(num5))
# Output: 9
