'''
415. Add Strings

Given two non-negative integers num1 and num2 represented as strings,
return their sum as a string.

You must not use any built-in library for handling large integers,
and you must not convert the inputs directly to integers.

Example 1:
    Input:
        num1 = "11"
        num2 = "123"

    Output:
        "134"

Example 2:
    Input:
        num1 = "456"
        num2 = "77"

    Output:
        "533"

Example 3:
    Input:
        num1 = "0"
        num2 = "0"

    Output:
        "0"

Constraints:
    1 <= num1.length, num2.length <= 10^4
    num1 and num2 consist of digits only.
    num1 and num2 do not have leading zeros except for the number 0 itself.
'''

# String + Math + Two Pointers

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1

        carry = 0
        result = []

        while pointer1 >= 0 or pointer2 >= 0 or carry:

            digit1 = ord(num1[pointer1]) - ord("0") if pointer1 >= 0 else 0
            digit2 = ord(num2[pointer2]) - ord("0") if pointer2 >= 0 else 0

            total = digit1 + digit2 + carry

            result.append(str(total % 10))
            carry = total // 10

            pointer1 -= 1
            pointer2 -= 1

        return "".join(reversed(result))


# Example usage
solution = Solution()

# Example 1
num1 = "11"
num2 = "123"
print(solution.addStrings(num1, num2))
# Output: "134"

# Example 2
num3 = "456"
num4 = "77"
print(solution.addStrings(num3, num4))
# Output: "533"

# Example 3
num5 = "0"
num6 = "0"
print(solution.addStrings(num5, num6))
# Output: "0"

# Example 4
num7 = "999"
num8 = "1"
print(solution.addStrings(num7, num8))
# Output: "1000"

# Example 5
num9 = "123456789123456789"
num10 = "987654321987654321"
print(solution.addStrings(num9, num10))
# Output: "1111111111111111110"

# Example 6
num11 = "5000"
num12 = "5000"
print(solution.addStrings(num11, num12))
# Output: "10000"
