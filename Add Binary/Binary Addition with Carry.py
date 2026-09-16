'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
    1 <= a.length, b.length <= 10^4
    1 <= b.length <= 10^4
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
'''

# Binary Addition with Carry
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        result = []

        while i >= 0 or j >= 0 or carry:

            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))

            carry = total // 2

        return ''.join(reversed(result))


# Example usage
solution = Solution()

print(solution.addBinary("11", "1"))  # Output: "100"
print(solution.addBinary("1010", "1011"))  # Output: "10101"
print(solution.addBinary("0", "0"))  # Output: "0"
print(solution.addBinary("1111", "1"))  # Output: "10000"
