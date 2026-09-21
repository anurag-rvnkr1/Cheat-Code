'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    - Starting with any positive integer, replace the number by the sum of the
      squares of its digits.
    - Repeat the process until the number equals 1, where it will stay.
    - If the process loops endlessly in a cycle that does not include 1,
      then the number is not a happy number.

Return True if n is a happy number, and False if not.

Example 1:
    Input: n = 19
    Output: True

Explanation:
    1² + 9² = 82
    8² + 2² = 68
    6² + 8² = 100
    1² + 0² + 0² = 1

Example 2:
    Input: n = 2
    Output: False

Constraints:
    1 <= n <= 2^31 - 1
'''

# Hash Set


class Solution:
    def happyNumber(self, n: int) -> bool:
        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1


# Example usage
solution = Solution()

# Example 1
n1 = 19
print(solution.happyNumber(n1))  # Output: True

# Example 2
n2 = 2
print(solution.happyNumber(n2))  # Output: False

# Example 3
n3 = 7
print(solution.happyNumber(n3))  # Output: True

# Example 4
n4 = 20
print(solution.happyNumber(n4))  # Output: False
