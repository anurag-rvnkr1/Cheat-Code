'''
371. Sum of Two Integers

Given two integers a and b, return the sum of the two integers
without using the operators '+' and '-'.

Example 1:
    Input:
        a = 1
        b = 2

    Output:
        3

Example 2:
    Input:
        a = 2
        b = 3

    Output:
        5

Constraints:
    -1000 <= a, b <= 1000
'''

# Bit Manipulation

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)


# Example usage
solution = Solution()

# Example 1
a1, b1 = 1, 2
print(solution.getSum(a1, b1))
# Output: 3

# Example 2
a2, b2 = 2, 3
print(solution.getSum(a2, b2))
# Output: 5

# Example 3
a3, b3 = -1, 1
print(solution.getSum(a3, b3))
# Output: 0

# Example 4
a4, b4 = -2, 3
print(solution.getSum(a4, b4))
# Output: 1

# Example 5
a5, b5 = -5, -7
print(solution.getSum(a5, b5))
# Output: -12

# Example 6
a6, b6 = 1000, -1000
print(solution.getSum(a6, b6))
# Output: 0
