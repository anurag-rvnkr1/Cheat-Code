'''
397. Integer Replacement

Given a positive integer n, return the minimum number of replacements
needed for n to become 1.

Operations:
    - If n is even, replace n with n / 2.
    - If n is odd, replace n with either n + 1 or n - 1.

Example 1:
    Input:
        n = 8

    Output:
        3

Explanation:
        8 -> 4 -> 2 -> 1

Example 2:
    Input:
        n = 7

    Output:
        4

Explanation:
        7 -> 8 -> 4 -> 2 -> 1

Example 3:
    Input:
        n = 4

    Output:
        2

Constraints:
    1 <= n <= 2^31 - 1
'''

# Greedy + Bit Manipulation

class Solution:
    def integerReplacement(self, n: int) -> int:
        operations = 0

        while n != 1:

            if n % 2 == 0:
                n //= 2

            else:
                # Special case for 3.
                if n == 3 or (n & 2) == 0:
                    n -= 1
                else:
                    n += 1

            operations += 1

        return operations


# Example usage
solution = Solution()

# Example 1
n1 = 8
print(solution.integerReplacement(n1))
# Output: 3

# Example 2
n2 = 7
print(solution.integerReplacement(n2))
# Output: 4

# Example 3
n3 = 4
print(solution.integerReplacement(n3))
# Output: 2

# Example 4
n4 = 3
print(solution.integerReplacement(n4))
# Output: 2

# Example 5
n5 = 15
print(solution.integerReplacement(n5))
# Output: 5

# Example 6
n6 = 2147483647
print(solution.integerReplacement(n6))
# Output: 32
