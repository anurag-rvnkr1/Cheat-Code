'''
204. Count Primes

Given an integer n, return the number of prime numbers that are strictly
less than n.

A prime number is a natural number greater than 1 that has exactly two
positive divisors: 1 and itself.

Example 1:
    Input: n = 10
    Output: 4

Explanation:
    There are 4 prime numbers less than 10: 2, 3, 5, and 7.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0

Constraints:
    0 <= n <= 5 * 10^6
'''

# Sieve of Eratosthenes

from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Assume all numbers are prime initially.
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        p = 2

        while p * p < n:
            if is_prime[p]:
                # Mark all multiples of p as non-prime.
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False

            p += 1

        return sum(is_prime)


# Example usage
solution = Solution()

# Example 1
n1 = 10
print(solution.countPrimes(n1))  # Output: 4

# Example 2
n2 = 0
print(solution.countPrimes(n2))  # Output: 0

# Example 3
n3 = 1
print(solution.countPrimes(n3))  # Output: 0

# Example 4
n4 = 20
print(solution.countPrimes(n4))  # Output: 8
