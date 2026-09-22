'''
342. Power of Four

Given an integer n, return True if it is a power of four.
Otherwise, return False.

An integer n is a power of four if there exists an integer x such that:

    n == 4^x

Example 1:
    Input:
        n = 16

    Output:
        True

Example 2:
    Input:
        n = 5

    Output:
        False

Example 3:
    Input:
        n = 1

    Output:
        True

Constraints:
    -2^31 <= n <= 2^31 - 1

Follow-up:
    Can you solve it without loops or recursion?
'''

# Bit Manipulation + Math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (
            n > 0 and
            (n & (n - 1)) == 0 and
            (n & 0x55555555) != 0
        )


# Example usage
solution = Solution()

# Example 1
n1 = 16
print(solution.isPowerOfFour(n1))
# Output: True

# Example 2
n2 = 5
print(solution.isPowerOfFour(n2))
# Output: False

# Example 3
n3 = 1
print(solution.isPowerOfFour(n3))
# Output: True

# Example 4
n4 = 64
print(solution.isPowerOfFour(n4))
# Output: True

# Example 5
n5 = 8
print(solution.isPowerOfFour(n5))
# Output: False

# Example 6
n6 = 256
print(solution.isPowerOfFour(n6))
# Output: True
