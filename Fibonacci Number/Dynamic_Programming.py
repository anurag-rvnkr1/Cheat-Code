'''
509. Fibonacci Number

The Fibonacci numbers are defined as:

    F(0) = 0
    F(1) = 1

For n > 1:

    F(n) = F(n - 1) + F(n - 2)

Given n, return F(n).

Example 1:
    Input:
        n = 2

    Output:
        1

Example 2:
    Input:
        n = 3

    Output:
        2

Example 3:
    Input:
        n = 4

    Output:
        3

Constraints:
    0 <= n <= 30
'''

# Dynamic Programming (Bottom-Up)

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        previous = 0
        current = 1

        for _ in range(2, n + 1):
            previous, current = current, previous + current

        return current


# -------------------------------------------------------
# Example Usage
# -------------------------------------------------------

solution = Solution()

# Example 1
print(solution.fib(2))
# Output: 1

# Example 2
print(solution.fib(3))
# Output: 2

# Example 3
print(solution.fib(4))
# Output: 3

# Example 4
print(solution.fib(0))
# Output: 0

# Example 5
print(solution.fib(1))
# Output: 1

# Example 6
print(solution.fib(10))
# Output: 55
