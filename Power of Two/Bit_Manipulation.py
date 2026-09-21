'''
231. Power of Two

Given an integer n, return True if it is a power of two. Otherwise, return False.

An integer n is a power of two if there exists an integer x such that:

    n == 2^x

Example 1:
    Input: n = 1
    Output: True

Explanation:
    2^0 = 1

Example 2:
    Input: n = 16
    Output: True

Explanation:
    2^4 = 16

Example 3:
    Input: n = 3
    Output: False

Constraints:
    -2^31 <= n <= 2^31 - 1

Follow-up:
    Could you solve it without loops or recursion?
'''

# Bit Manipulation


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Power of two has exactly one set bit.
        return n > 0 and (n & (n - 1)) == 0


# Example usage
solution = Solution()

# Example 1
n1 = 1
print(solution.isPowerOfTwo(n1))  # Output: True

# Example 2
n2 = 16
print(solution.isPowerOfTwo(n2))  # Output: True

# Example 3
n3 = 3
print(solution.isPowerOfTwo(n3))  # Output: False

# Example 4
n4 = 64
print(solution.isPowerOfTwo(n4))  # Output: True

# Example 5
n5 = -16
print(solution.isPowerOfTwo(n5))  # Output: False

# Example 6
n6 = 0
print(solution.isPowerOfTwo(n6))  # Output: False
