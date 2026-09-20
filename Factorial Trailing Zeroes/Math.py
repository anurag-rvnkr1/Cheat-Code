'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note:
    n! = n × (n - 1) × (n - 2) × ... × 2 × 1

Trailing zeroes are created by pairs of (2 × 5). Since there are always
more factors of 2 than 5 in a factorial, count the number of factors of 5.

Example 1:
    Input: n = 3
    Output: 0

Explanation:
    3! = 6, which has no trailing zeroes.

Example 2:
    Input: n = 5
    Output: 1

Explanation:
    5! = 120, which has one trailing zero.

Example 3:
    Input: n = 30
    Output: 7

Explanation:
    30! has 7 trailing zeroes.

Constraints:
    0 <= n <= 10^4
'''

# Math


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0

        while n > 0:
            n //= 5
            zeroes += n

        return zeroes


# Example usage
solution = Solution()

# Example 1
n1 = 3
print(solution.trailingZeroes(n1))  # Output: 0

# Example 2
n2 = 5
print(solution.trailingZeroes(n2))  # Output: 1

# Example 3
n3 = 30
print(solution.trailingZeroes(n3))  # Output: 7

# Example 4
n4 = 100
print(solution.trailingZeroes(n4))  # Output: 24
