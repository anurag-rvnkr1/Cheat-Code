'''
246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated
180 degrees (looked at upside down).

Given a string num representing a number, return True if it is
strobogrammatic, otherwise return False.

Valid rotation pairs are:
    0 ↔ 0
    1 ↔ 1
    6 ↔ 9
    8 ↔ 8
    9 ↔ 6

Example 1:
    Input: num = "69"
    Output: True

Example 2:
    Input: num = "88"
    Output: True

Example 3:
    Input: num = "962"
    Output: False

Constraints:
    1 <= num.length <= 50
    num consists of digits only.
'''

# Two Pointers + String


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotation = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        left = 0
        right = len(num) - 1

        while left <= right:

            # Invalid digit.
            if num[left] not in rotation:
                return False

            # Rotated value must match opposite pointer.
            if rotation[num[left]] != num[right]:
                return False

            left += 1
            right -= 1

        return True


# Example usage
solution = Solution()

# Example 1
num1 = "69"
print(solution.isStrobogrammatic(num1))  # Output: True

# Example 2
num2 = "88"
print(solution.isStrobogrammatic(num2))  # Output: True

# Example 3
num3 = "962"
print(solution.isStrobogrammatic(num3))  # Output: False

# Example 4
num4 = "818"
print(solution.isStrobogrammatic(num4))  # Output: True

# Example 5
num5 = "101"
print(solution.isStrobogrammatic(num5))  # Output: True

# Example 6
num6 = "25"
print(solution.isStrobogrammatic(num6))  # Output: False
