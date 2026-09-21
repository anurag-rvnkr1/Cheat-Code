'''
264. Ugly Number II

An ugly number is a positive integer whose prime factors are limited to
2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:
    Input: n = 10
    Output: 12

Explanation:
    The first 10 ugly numbers are:
    [1,2,3,4,5,6,8,9,10,12]

Example 2:
    Input: n = 1
    Output: 1

Constraints:
    1 <= n <= 1690
'''

# Dynamic Programming + Three Pointers


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n

        # Pointers for multiples of 2, 3, and 5.
        p2 = 0
        p3 = 0
        p5 = 0

        for i in range(1, n):
            next2 = ugly[p2] * 2
            next3 = ugly[p3] * 3
            next5 = ugly[p5] * 5

            next_ugly = min(next2, next3, next5)
            ugly[i] = next_ugly

            # Move every pointer that generated the current ugly number.
            if next_ugly == next2:
                p2 += 1

            if next_ugly == next3:
                p3 += 1

            if next_ugly == next5:
                p5 += 1

        return ugly[-1]


# Example usage
solution = Solution()

# Example 1
n1 = 10
print(solution.nthUglyNumber(n1))
# Output: 12

# Example 2
n2 = 1
print(solution.nthUglyNumber(n2))
# Output: 1

# Example 3
n3 = 15
print(solution.nthUglyNumber(n3))
# Output: 24

# Example 4
n4 = 20
print(solution.nthUglyNumber(n4))
# Output: 36

# Example 5
n5 = 1690
print(solution.nthUglyNumber(n5))
# Output: 2123366400
