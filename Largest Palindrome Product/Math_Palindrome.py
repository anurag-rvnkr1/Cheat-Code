'''
479. Largest Palindrome Product

Given an integer n, return the largest palindrome made from the product of two
n-digit numbers.

Since the answer can be very large, return it modulo 1337.

Example 1:
    Input:
        n = 2

    Output:
        987

Explanation:
        Largest palindrome = 9009 = 91 × 99
        9009 % 1337 = 987

Example 2:
    Input:
        n = 1

    Output:
        9

Constraints:
    1 <= n <= 8
'''

# Math + Palindrome Construction


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10 ** n - 1
        lower = 10 ** (n - 1)

        # Construct palindromes from the first half.
        for first_half in range(upper, lower - 1, -1):
            palindrome = int(
                str(first_half) + str(first_half)[::-1]
            )

            divisor = upper

            while divisor * divisor >= palindrome:
                if palindrome % divisor == 0:
                    quotient = palindrome // divisor

                    if lower <= quotient <= upper:
                        return palindrome % 1337

                divisor -= 1

        return -1


# Example usage
solution = Solution()

# Example 1
print(solution.largestPalindrome(2))
# Output: 987

# Example 2
print(solution.largestPalindrome(1))
# Output: 9

# Example 3
print(solution.largestPalindrome(3))
# Output: 123

# Example 4
print(solution.largestPalindrome(4))
# Output: 597

# Example 5
print(solution.largestPalindrome(5))
# Output: 677

# Example 6
print(solution.largestPalindrome(6))
# Output: 1218
