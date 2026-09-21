'''
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to
2, 3, and 5.

Given an integer n, return True if n is an ugly number, otherwise return False.

Example 1:
    Input: n = 6
    Output: True

Explanation:
    6 = 2 × 3

Example 2:
    Input: n = 1
    Output: True

Explanation:
    1 has no prime factors, therefore it is considered an ugly number.

Example 3:
    Input: n = 14
    Output: False

Explanation:
    14 = 2 × 7
    Since 7 is not one of the allowed prime factors, 14 is not ugly.

Constraints:
    -2^31 <= n <= 2^31 - 1
'''

# Math


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # Remove all factors of 2, 3, and 5.
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        # If only allowed prime factors existed, n becomes 1.
        return n == 1


# Example usage
solution = Solution()

# Example 1
n1 = 6
print(solution.isUgly(n1))
# Output: True

# Example 2
n2 = 1
print(solution.isUgly(n2))
# Output: True

# Example 3
n3 = 14
print(solution.isUgly(n3))
# Output: False

# Example 4
n4 = 30
print(solution.isUgly(n4))
# Output: True

# Example 5
n5 = 25
print(solution.isUgly(n5))
# Output: True

# Example 6
n6 = -6
print(solution.isUgly(n6))
# Output: False

# Example 7
n7 = 7
print(solution.isUgly(n7))
# Output: False
