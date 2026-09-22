'''
405. Convert a Number to Hexadecimal

Given a 32-bit signed integer num, return its hexadecimal representation.

For negative integers, two's complement representation is used.

Do not use any built-in library method that directly converts numbers to hexadecimal.

Example 1:
    Input:
        num = 26

    Output:
        "1a"

Example 2:
    Input:
        num = -1

    Output:
        "ffffffff"

Constraints:
    -2^31 <= num <= 2^31 - 1
'''

# Bit Manipulation

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_digits = "0123456789abcdef"

        # Convert negative number to unsigned 32-bit integer.
        if num < 0:
            num += 2 ** 32

        result = []

        while num > 0:
            result.append(hex_digits[num & 15])
            num >>= 4

        return "".join(reversed(result))


# Example usage
solution = Solution()

# Example 1
num1 = 26
print(solution.toHex(num1))
# Output: "1a"

# Example 2
num2 = -1
print(solution.toHex(num2))
# Output: "ffffffff"

# Example 3
num3 = 0
print(solution.toHex(num3))
# Output: "0"

# Example 4
num4 = 16
print(solution.toHex(num4))
# Output: "10"

# Example 5
num5 = -26
print(solution.toHex(num5))
# Output: "ffffffe6"

# Example 6
num6 = 305419896
print(solution.toHex(num6))
# Output: "12345678"
