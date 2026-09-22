'''
313. Super Ugly Number

A super ugly number is a positive integer whose prime factors are in the
given array primes.

Given an integer n and an array primes, return the nth super ugly number.

Example 1:
    Input:
        n = 12
        primes = [2,7,13,19]

    Output:
        32

Explanation:
    First 12 super ugly numbers are:
    [1,2,4,7,8,13,14,16,19,26,28,32]

Example 2:
    Input:
        n = 1
        primes = [2,3,5]

    Output:
        1

Constraints:
    1 <= n <= 10^5
    1 <= primes.length <= 100
    2 <= primes[i] <= 1000
    primes is sorted in ascending order.
'''

# Heap + Dynamic Programming

from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n

        # Heap stores: (next_value, prime, index_in_ugly)
        heap = []

        for prime in primes:
            heapq.heappush(heap, (prime, prime, 0))

        for i in range(1, n):
            ugly[i] = heap[0][0]

            # Remove all duplicates producing the same ugly number.
            while heap and heap[0][0] == ugly[i]:
                value, prime, index = heapq.heappop(heap)

                index += 1
                heapq.heappush(
                    heap,
                    (prime * ugly[index], prime, index)
                )

        return ugly[-1]


# Example usage
solution = Solution()

# Example 1
n1 = 12
primes1 = [2, 7, 13, 19]
print(solution.nthSuperUglyNumber(n1, primes1))
# Output: 32

# Example 2
n2 = 1
primes2 = [2, 3, 5]
print(solution.nthSuperUglyNumber(n2, primes2))
# Output: 1

# Example 3
n3 = 15
primes3 = [3, 5, 7]
print(solution.nthSuperUglyNumber(n3, primes3))
# Output: 81

# Example 4
n4 = 10
primes4 = [2]
print(solution.nthSuperUglyNumber(n4, primes4))
# Output: 512

# Example 5
n5 = 8
primes5 = [2, 11]
print(solution.nthSuperUglyNumber(n5, primes5))
# Output: 64
