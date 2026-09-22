'''
357. Count Numbers with Unique Digits

Given an integer n, return the count of all numbers with unique digits,
x, where 0 <= x < 10^n.

Example 1:
    Input:
        n = 2

    Output:
        91

Explanation:
        There are 91 numbers with unique digits in the range [0, 100).

Example 2:
    Input:
        n = 0

    Output:
        1

Constraints:
    0 <= n <= 8
'''

# Dynamic Programming + Math (Permutation Counting)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        # Count for n = 1
        total = 10
        unique_digits = 9
        available_digits = 9

        # Count for n >= 2
        for _ in range(2, n + 1):
            unique_digits *= available_digits
            total += unique_digits
            available_digits -= 1

        return total


# Example usage
solution = Solution()

# Example 1
n1 = 2
print(solution.countNumbersWithUniqueDigits(n1))
# Output: 91

# Example 2
n2 = 0
print(solution.countNumbersWithUniqueDigits(n2))
# Output: 1

# Example 3
n3 = 1
print(solution.countNumbersWithUniqueDigits(n3))
# Output: 10

# Example 4
n4 = 3
print(solution.countNumbersWithUniqueDigits(n4))
# Output: 739

# Example 5
n5 = 4
print(solution.countNumbersWithUniqueDigits(n5))
# Output: 5275

# Example 6
n6 = 8
print(solution.countNumbersWithUniqueDigits(n6))
# Output: 2345851
