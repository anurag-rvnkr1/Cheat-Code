'''
400. Nth Digit

Given an integer n, return the nth digit of the infinite integer sequence:

    12345678910111213141516...

Example 1:
    Input:
        n = 3

    Output:
        3

Example 2:
    Input:
        n = 11

    Output:
        0

Explanation:
        The 11th digit is the '0' in number 10.

Example 3:
    Input:
        n = 190

    Output:
        1

Constraints:
    1 <= n <= 2^31 - 1
'''

# Math + Number Theory

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_length = 1
        count = 9
        start = 1

        # Find the digit length group containing the nth digit.
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Find the exact number containing the digit.
        number = start + (n - 1) // digit_length

        # Find the digit index inside that number.
        digit_index = (n - 1) % digit_length

        return int(str(number)[digit_index])


# Example usage
solution = Solution()

# Example 1
n1 = 3
print(solution.findNthDigit(n1))
# Output: 3

# Example 2
n2 = 11
print(solution.findNthDigit(n2))
# Output: 0

# Example 3
n3 = 190
print(solution.findNthDigit(n3))
# Output: 1

# Example 4
n4 = 250
print(solution.findNthDigit(n4))
# Output: 1

# Example 5
n5 = 1000
print(solution.findNthDigit(n5))
# Output: 3

# Example 6
n6 = 2147483647
print(solution.findNthDigit(n6))
# Output: 2
