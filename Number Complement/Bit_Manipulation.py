'''
476. Number Complement

The complement of an integer is obtained by flipping all the bits in its binary
representation, excluding leading zeros.

Given a positive integer num, return its complement.

Example 1:
    Input:
        num = 5

    Output:
        2

Explanation:
        5  -> 101
        2  -> 010

Example 2:
    Input:
        num = 1

    Output:
        0

Constraints:
    1 <= num < 2^31
'''

# Bit Manipulation


class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1

        while mask <= num:
            mask <<= 1

        return (mask - 1) ^ num


# Example usage
solution = Solution()

# Example 1
num1 = 5
print(solution.findComplement(num1))
# Output: 2

# Example 2
num2 = 1
print(solution.findComplement(num2))
# Output: 0

# Example 3
num3 = 2
print(solution.findComplement(num3))
# Output: 1

# Example 4
num4 = 10
print(solution.findComplement(num4))
# Output: 5

# Example 5
num5 = 7
print(solution.findComplement(num5))
# Output: 0

# Example 6
num6 = 100
print(solution.findComplement(num6))
# Output: 27
